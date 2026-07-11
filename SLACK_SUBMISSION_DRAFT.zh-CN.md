# Slack Agent Builder Devpost 提交草稿

## Project name

CupSafe Slack Desk

## Tagline

A Slack agent that helps support and security teams triage wallet-risk incidents before a user signs.

## Inspiration

Wallet users often ask support teams whether they should approve a contract, bridge funds, swap through a route, or pay a merchant. The risky moment often happens inside a support conversation, not inside a wallet UI. CupSafe Slack Desk brings the risk memory workflow into Slack so the team can respond before the user signs.

## What it does

CupSafe Slack Desk reads a Slack-style incident report, extracts the operation, amount, recipient trust, and route risk, retrieves similar risk memories, and returns an `ALLOW`, `REVIEW`, or `DENY` decision. It also drafts a concise support reply and tells the team whether to escalate the incident to security.

## How we built it

The current prototype is a local Slack-style demo built with static HTML, CSS, and JavaScript. The decision engine reuses the CupSafe risk-memory pattern from prior CupSafe submissions. A real Slack integration path is documented with `/cupsafe-check`, Slack message shortcuts, a hosted endpoint, and judge sandbox access.

## Accomplishments

- Created deterministic Slack incident fixtures.
- Built a Slack-like local demo UI.
- Implemented explainable `ALLOW` / `REVIEW` / `DENY` decisions.
- Added support-reply and security-escalation generation.
- Added a verification script that checks all expected decisions.

## What is next

- Create a real Slack app in a developer sandbox.
- Add `/cupsafe-check` and message shortcut support.
- Host the agent endpoint.
- Give judges access to the Slack developer sandbox.
- Add durable incident memory for repeated scam and false-positive patterns.

## Links to prepare

- Public repository: TBD
- Demo URL: TBD
- Video URL: TBD
- Slack developer sandbox URL: requires user-authorized Slack workspace/app setup

## Notes

No wallet, private key, seed phrase, KYC, payment, or transaction signing is used in this prototype.
