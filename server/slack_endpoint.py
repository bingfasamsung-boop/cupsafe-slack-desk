from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs
import json
import os
import re
import time


MEMORY = [
    {
        "title": "Unknown approval drain pattern",
        "operation": "approve",
        "recipientTrust": "unknown",
        "amountBand": "high",
        "tags": ["approval", "dm", "allowance"],
        "decision": "DENY",
        "evidence": "Unknown allowance requests can drain funds after a single signature.",
        "reply": "Tell the user not to sign. Ask them to verify the contract from official project channels only.",
    },
    {
        "title": "Verified merchant small payment",
        "operation": "transfer",
        "recipientTrust": "verified",
        "amountBand": "low",
        "tags": ["merchant", "low-risk"],
        "decision": "ALLOW",
        "evidence": "Small payments to verified merchants were previously allowed when they stayed under cap.",
        "reply": "Confirm the merchant name and proceed only if the checkout domain is expected.",
    },
    {
        "title": "Bridge finality review",
        "operation": "bridge",
        "recipientTrust": "known",
        "amountBand": "medium",
        "tags": ["bridge", "finality", "route"],
        "decision": "REVIEW",
        "evidence": "Bridge actions add route, destination-chain, and finality risk even when the provider is known.",
        "reply": "Ask the user to confirm destination chain, recipient address, bridge status, and expected arrival time.",
    },
    {
        "title": "High slippage swap",
        "operation": "swap",
        "recipientTrust": "known",
        "amountBand": "medium",
        "tags": ["swap", "slippage", "liquidity"],
        "decision": "REVIEW",
        "evidence": "High slippage can indicate thin liquidity, price impact, or a malicious route.",
        "reply": "Ask the user to reduce slippage, split the swap, or use a deeper verified route.",
    },
]


def amount_band(amount, cap):
    if amount > cap:
        return "high"
    if amount >= cap * 0.4:
        return "medium"
    return "low"


def infer_operation(text):
    if any(word in text for word in ("approve", "approval", "allowance")):
        return "approve"
    if "bridge" in text:
        return "bridge"
    if "swap" in text or "slippage" in text:
        return "swap"
    return "transfer"


def infer_amount(text):
    match = re.search(r"(?:\$|usd|usdt)?\s*(\d+(?:\.\d+)?)\s*(?:usdt|usd|\$)?", text)
    return float(match.group(1)) if match else 10.0


def infer_recipient_trust(text):
    if "verified" in text or "merchant" in text:
        return "verified"
    if "known" in text or "trusted" in text:
        return "known"
    return "unknown"


def infer_slippage_bps(text):
    bps = re.search(r"(\d+(?:\.\d+)?)\s*bps", text)
    if bps:
        return float(bps.group(1))
    percent = re.search(r"(\d+(?:\.\d+)?)\s*%\s*slippage|slippage\s*(\d+(?:\.\d+)?)\s*%", text)
    if percent:
        return float(percent.group(1) or percent.group(2)) * 100
    return 0.0


def score_memory(incident, memory):
    score = 0
    if incident["operation"] == memory["operation"]:
        score += 40
    if incident["recipientTrust"] == memory["recipientTrust"]:
        score += 22
    if amount_band(incident["amount"], incident["dailyCap"]) == memory["amountBand"]:
        score += 18
    if "telegram" in incident["message"].lower() and "dm" in memory["tags"]:
        score += 10
    if incident["slippageBps"] >= 500 and "slippage" in memory["tags"]:
        score += 14
    if incident["operation"] == "bridge" and "finality" in memory["tags"]:
        score += 14
    return score


def decide(incident, top_memory):
    if incident["operation"] == "approve" and incident["recipientTrust"] != "verified":
        return "DENY"
    if incident["amount"] > incident["dailyCap"]:
        return "DENY"
    if incident["operation"] == "swap" and incident["slippageBps"] >= 500:
        return "REVIEW"
    if incident["operation"] == "bridge":
        return "REVIEW"
    return top_memory.get("decision", "REVIEW")


def severity_for(decision, incident):
    if decision == "DENY":
        return "critical"
    if incident["operation"] == "bridge" or incident["slippageBps"] >= 500:
        return "elevated"
    if decision == "REVIEW":
        return "medium"
    return "low"


def parse_slack_text(text):
    raw = (text or "").strip()
    lower = raw.lower()
    return {
        "id": f"slash-{int(time.time())}",
        "channel": "#wallet-support",
        "reporter": "slack-user",
        "message": raw or "Manual wallet-risk check requested from Slack.",
        "operation": infer_operation(lower),
        "amount": infer_amount(lower),
        "dailyCap": 25.0,
        "recipientTrust": infer_recipient_trust(lower),
        "slippageBps": infer_slippage_bps(lower),
    }


def triage(incident):
    retrieved = sorted(
        [{**item, "similarity": score_memory(incident, item)} for item in MEMORY],
        key=lambda item: item["similarity"],
        reverse=True,
    )[:3]
    top = retrieved[0]
    decision = decide(incident, top)
    severity = severity_for(decision, incident)
    if decision == "ALLOW":
        escalation = "No security escalation. Keep the support thread open until the user confirms the merchant/domain."
    elif decision == "DENY":
        escalation = f"Escalate to #security-triage with incident={incident['id']}, reason=blocked signature risk."
    else:
        escalation = f"Escalate only if user cannot verify route/address. Add incident={incident['id']} to the review queue."
    return decision, severity, retrieved, escalation


def slack_response_for(text):
    incident = parse_slack_text(text)
    decision, severity, retrieved, escalation = triage(incident)
    top = retrieved[0]
    summary = f"{decision}: {incident['operation']} for {incident['amount']:g} USDT in {incident['channel']}"
    support_reply = top["reply"]
    return {
        "response_type": "ephemeral",
        "text": summary,
        "blocks": [
            {"type": "section", "text": {"type": "mrkdwn", "text": f"*CupSafe {decision}* ({severity})\n{incident['message']}"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": f"*Memory match:* {top['title']}\n{top['evidence']}"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": f"*Support reply:*\n{support_reply}"}},
            {"type": "context", "elements": [{"type": "mrkdwn", "text": escalation}]},
        ],
    }


class Handler(BaseHTTPRequestHandler):
    def _send_json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("content-type", "application/json; charset=utf-8")
        self.send_header("cache-control", "no-store")
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ("/", "/health"):
            self._send_json(200, {"ok": True, "service": "cupsafe-slack-desk", "endpoint": "/slack/commands"})
            return
        self._send_json(404, {"ok": False, "error": "not_found"})

    def do_POST(self):
        if self.path != "/slack/commands":
            self._send_json(404, {"ok": False, "error": "not_found"})
            return
        length = int(self.headers.get("content-length", "0"))
        params = parse_qs(self.rfile.read(length).decode("utf-8"))
        text = params.get("text", [""])[0]
        self._send_json(200, slack_response_for(text))

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args))


def main():
    port = int(os.environ.get("PORT", "8787"))
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"CupSafe Slack endpoint listening on http://127.0.0.1:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
