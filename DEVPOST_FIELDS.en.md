# Devpost Fields - CupSafe Slack Desk

## Project Name

CupSafe Slack Desk

## Elevator Pitch

CupSafe Slack Desk is a Slack agent that helps support, payments, and security teams triage wallet-risk incidents before a user signs.

## Inspiration

Users often ask for help inside support channels at the exact moment they are about to approve a contract, bridge funds, swap through a risky route, or pay a merchant. Support teams need a fast way to turn scattered incident context into a clear answer. CupSafe Slack Desk brings wallet-risk memory into Slack so teams can respond with evidence before the user signs.

## What it does

The demo reads Slack-style incident reports, extracts wallet-risk features, retrieves similar risk memories, and returns `ALLOW`, `REVIEW`, or `DENY`. It also drafts a support-safe reply and explains whether the case should be escalated to security.

## How we built it

The prototype is an offline Slack-style app built with HTML, CSS, and JavaScript. The agent simulator uses deterministic fixtures for approval, merchant payment, bridge, and high-slippage swap incidents. We also prepared a Slack app manifest path for `/cupsafe-check`, message actions, and judge sandbox access.

## Challenges

The main challenge was making the agent useful without connecting to private wallets or real customer data. The demo uses explainable risk memories and synthetic incidents so judges can inspect the behavior safely.

## Accomplishments

- Built a Slack-style demo UI.
- Implemented an explainable wallet-risk triage engine.
- Added four deterministic incident fixtures.
- Added support replies and escalation logic.
- Added architecture, transcript, and verification materials.

## What is next

- Create a real Slack app in a developer sandbox.
- Connect `/cupsafe-check` to a hosted endpoint.
- Give judges access to the sandbox.
- Store confirmed scam and false-positive incidents as durable team memory.

## Built With

JavaScript, HTML, CSS, Slack app manifest draft, CupSafe risk-memory fixtures.

## Links

- Demo URL: TBD
- Source Code: TBD
- Video Demo: TBD
- Slack Developer Sandbox URL: requires user-authorized setup
