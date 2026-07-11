# CupSafe Slack Desk

CupSafe Slack Desk is a local prototype for the Slack Agent Builder Challenge. It adapts the CupSafe wallet-risk workflow into Slack so support, security, and operations teams can triage USDt and DeFi incidents before a user signs.

## What It Does

- Reads a Slack-style incident report.
- Retrieves similar risk memories.
- Scores the request as `ALLOW`, `REVIEW`, or `DENY`.
- Generates a support reply for the thread.
- Suggests whether to escalate to `#security-triage`.

## Files

- `index.html` - Slack-style offline demo.
- `src/slack-agent-sim.js` - local agent and policy logic.
- `data/slack-incidents.json` - demo incidents and expected decisions.
- `scripts/verify-slack-demo.mjs` - deterministic verification script.
- `slack/transcripts.md` - demo conversation flows.
- `ARCHITECTURE.md` - system architecture and real Slack integration path.
- `SLACK_SUBMISSION_DRAFT.zh-CN.md` - Devpost submission draft.
- `DEMO_VIDEO_SCRIPT.md` - short demo video script.

## Run Locally

```powershell
cd outputs/slack-cupsafe-desk
python -m http.server 8096
```

Open:

```text
http://127.0.0.1:8096/
```

Hosted demo:

```text
https://bingfasamsung-boop.github.io/cupsafe-slack-desk/
```

Source repository:

```text
https://github.com/bingfasamsung-boop/cupsafe-slack-desk
```

Verify decisions:

```powershell
npm run verify
```

## Scope

This is an offline demo. It does not connect to a real Slack workspace, does not use a Slack token, does not connect a wallet, does not sign transactions, and does not read private keys.
