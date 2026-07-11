# CupSafe Slack Desk Demo Video Script

Target length: 90-120 seconds.

## 0-15s - Problem

Support teams receive urgent wallet-risk questions in Slack: "Should this user approve a contract?", "Is this bridge route safe?", "Why is this swap slippage so high?"

## 15-35s - Agent Surface

Show the Slack-style demo. Pick the unknown approval incident in `#wallet-support`.

Narration: CupSafe Slack Desk reads the incident, extracts operation, amount, recipient trust, and the support question.

## 35-60s - Risk Memory

Run triage. Show the retrieved memory rows and `DENY` decision.

Narration: The agent matches the incident to a known approval-drain pattern and explains why the support team should tell the user not to sign.

## 60-85s - Other Decisions

Switch to the verified merchant and bridge examples.

Narration: Low-risk verified merchant payments can be allowed; bridges and high-slippage swaps are routed to review.

## 85-110s - Slack Integration Path

Show `ARCHITECTURE.md`.

Narration: The real Slack path is `/cupsafe-check`, message shortcuts, a hosted endpoint, and judge access to a developer sandbox.

## 110-120s - Close

CupSafe Slack Desk turns wallet-risk memory into fast, explainable Slack support decisions before a user signs.
