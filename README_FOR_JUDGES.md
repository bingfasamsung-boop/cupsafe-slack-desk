# CupSafe Slack Desk - Judge Notes

CupSafe Slack Desk is a Slack agent concept for support, payments, and security
teams that need to triage wallet-risk incidents before a user signs.

## Safe demo posture

This demo uses synthetic incident reports and fixture memory. It does not ask
for private keys, seed phrases, wallet connections, real customer data, or live
transaction signing.

## Core behavior

The agent classifies incidents as:

- `ALLOW`: known safe context, bounded approval.
- `REVIEW`: enough risk to escalate before signing.
- `DENY`: unsafe approval, phishing, impersonation, or prior scam memory.

Each response includes a severity level, evidence, and a support-safe reply.

## Local review

Open the local demo:

`http://127.0.0.1:8096/`

Run verification:

```bash
node scripts/verify-slack-demo.mjs
```

Expected result: four fixture incidents pass with the expected decisions.

## Production path

The intended Slack version uses `/cupsafe-check` and message actions to send
incident text to a hosted endpoint. A sandbox workspace would be shared with
judges after user-approved Slack app setup.
