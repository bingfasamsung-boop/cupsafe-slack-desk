# Security Boundary

This repository contains a public hackathon demo package only.

It does not include:

- Slack tokens or signing secrets.
- Wallet private keys, seed phrases, or wallet files.
- Browser password-store data.
- Real customer support messages.
- Live transaction signing, wallet connections, KYC, payment, or trading logic.

The current demo is safe to review as a static local or hosted prototype. A real
Slack installation must use secrets from the target deployment environment and
must not commit them to the repository.

## Demo endpoint boundary

- The optional `server/slack_endpoint.py` service is a low-risk demo endpoint for `/cupsafe-check`.
- It accepts Slack slash-command form fields and returns an ephemeral Slack JSON response.
- It does not store Slack tokens, signing secrets, verification tokens, private wallet data, or customer records.
- It does not verify Slack request signatures because no Slack signing secret is stored in this repository.
- For production use, add Slack request-signature verification and move runtime secrets into a managed secret store.
