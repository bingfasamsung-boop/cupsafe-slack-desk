# CupSafe Slack Desk Architecture

```text
Slack channel / command
        |
        v
CupSafe Slack Desk agent
        |
        +-- Incident parser
        +-- Policy scorer
        +-- Risk memory retrieval
        +-- Support reply generator
        |
        v
Slack thread reply + optional security escalation
```

## Components

- Slack surface: `/cupsafe-check`, message shortcut, or channel mention.
- Incident parser: extracts operation, amount, recipient trust, slippage, and support question.
- Risk memory: local JSON fixtures in the demo; can later be moved to a datastore.
- Policy scorer: returns `ALLOW`, `REVIEW`, or `DENY`.
- Slack reply generator: formats a concise message for support and security teams.

## Real integration path

1. Create a Slack app in a developer sandbox.
2. Add a slash command such as `/cupsafe-check`.
3. Connect the command to a hosted endpoint.
4. Store incident outcomes as review memory.
5. Give hackathon judges access to the sandbox workspace.

No Slack token, wallet key, or private user data is included in this local demo.
