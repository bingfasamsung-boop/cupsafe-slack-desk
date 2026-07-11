const MEMORY = [
  {
    title: "Unknown approval drain pattern",
    operation: "approve",
    recipientTrust: "unknown",
    amountBand: "high",
    tags: ["approval", "dm", "allowance"],
    decision: "DENY",
    evidence: "Unknown allowance requests can drain funds after a single signature.",
    reply: "Tell the user not to sign. Ask them to verify the contract from official project channels only."
  },
  {
    title: "Verified merchant small payment",
    operation: "transfer",
    recipientTrust: "verified",
    amountBand: "low",
    tags: ["merchant", "low-risk"],
    decision: "ALLOW",
    evidence: "Small payments to verified merchants were previously allowed when they stayed under cap.",
    reply: "Confirm the merchant name and proceed only if the checkout domain is expected."
  },
  {
    title: "Bridge finality review",
    operation: "bridge",
    recipientTrust: "known",
    amountBand: "medium",
    tags: ["bridge", "finality", "route"],
    decision: "REVIEW",
    evidence: "Bridge actions add route, destination-chain, and finality risk even when the provider is known.",
    reply: "Ask the user to confirm destination chain, recipient address, bridge status, and expected arrival time."
  },
  {
    title: "High slippage swap",
    operation: "swap",
    recipientTrust: "known",
    amountBand: "medium",
    tags: ["swap", "slippage", "liquidity"],
    decision: "REVIEW",
    evidence: "High slippage can indicate thin liquidity, price impact, or a malicious route.",
    reply: "Ask the user to reduce slippage, split the swap, or use a deeper verified route."
  }
];

export function triageSlackIncident(incident) {
  const normalized = normalizeIncident(incident);
  const retrieved = MEMORY
    .map((item) => ({ ...item, similarity: scoreMemory(normalized, item) }))
    .sort((a, b) => b.similarity - a.similarity)
    .slice(0, 3);
  const decision = decide(normalized, retrieved[0]);
  const severity = severityFor(decision, normalized);

  return {
    id: normalized.id,
    decision,
    severity,
    summary: `${decision}: ${normalized.operation} for ${normalized.amount} USDT in ${normalized.channel}`,
    slackReply: buildSlackReply(normalized, decision, severity, retrieved),
    escalation: buildEscalation(normalized, decision, severity),
    retrieved
  };
}

export function runDeskDataset(incidents) {
  return incidents.map((incident) => ({
    incident,
    result: triageSlackIncident(incident)
  }));
}

function normalizeIncident(incident) {
  return {
    id: incident.id || "manual-check",
    channel: incident.channel || "#wallet-support",
    reporter: incident.reporter || "support-agent",
    message: incident.message || "",
    operation: incident.operation || "transfer",
    amount: Number(incident.amount || 0),
    dailyCap: Number(incident.dailyCap || 25),
    recipientTrust: incident.recipientTrust || "unknown",
    slippageBps: Number(incident.slippageBps || 0),
    customerNeed: incident.customerNeed || "Need a safe support reply."
  };
}

function scoreMemory(incident, memory) {
  let score = 0;
  if (incident.operation === memory.operation) score += 40;
  if (incident.recipientTrust === memory.recipientTrust) score += 22;
  if (amountBand(incident.amount, incident.dailyCap) === memory.amountBand) score += 18;
  if (incident.message.toLowerCase().includes("telegram") && memory.tags.includes("dm")) score += 10;
  if (incident.slippageBps >= 500 && memory.tags.includes("slippage")) score += 14;
  if (incident.operation === "bridge" && memory.tags.includes("finality")) score += 14;
  return score;
}

function decide(incident, topMemory) {
  if (incident.operation === "approve" && incident.recipientTrust !== "verified") return "DENY";
  if (incident.amount > incident.dailyCap) return "DENY";
  if (incident.operation === "swap" && incident.slippageBps >= 500) return "REVIEW";
  if (incident.operation === "bridge") return "REVIEW";
  return topMemory?.decision || "REVIEW";
}

function amountBand(amount, cap) {
  if (amount > cap) return "high";
  if (amount >= cap * 0.4) return "medium";
  return "low";
}

function severityFor(decision, incident) {
  if (decision === "DENY") return "critical";
  if (incident.operation === "bridge" || incident.slippageBps >= 500) return "elevated";
  if (decision === "REVIEW") return "medium";
  return "low";
}

function buildSlackReply(incident, decision, severity, retrieved) {
  const top = retrieved[0];
  const actionLine = actionFor(decision, top);
  return [
    `:${emojiFor(decision)}: *CupSafe ${decision}* (${severity})`,
    `Request: ${incident.message}`,
    `Memory match: ${top?.title || "No strong match"} - ${top?.evidence || "Manual review needed."}`,
    `Support reply: ${actionLine}`
  ].join("\n");
}

function buildEscalation(incident, decision, severity) {
  if (decision === "ALLOW") {
    return "No security escalation. Keep the support thread open until the user confirms the merchant/domain.";
  }
  if (decision === "DENY") {
    return `Escalate to #security-triage with incident=${incident.id}, reporter=${incident.reporter}, reason=blocked signature risk.`;
  }
  return `Escalate only if user cannot verify route/address. Add incident=${incident.id} to the review queue.`;
}

function actionFor(decision, top) {
  if (decision === "DENY") return top?.reply || "Tell the user not to sign and verify official links.";
  if (decision === "REVIEW") return top?.reply || "Ask for more context before the user signs.";
  return top?.reply || "Proceed with standard confirmation.";
}

function emojiFor(decision) {
  if (decision === "DENY") return "octagonal_sign";
  if (decision === "REVIEW") return "warning";
  return "white_check_mark";
}
