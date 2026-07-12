# Deployment Status

## Public links

- Source repository: https://github.com/bingfasamsung-boop/cupsafe-slack-desk
- Hosted static demo: https://bingfasamsung-boop.github.io/cupsafe-slack-desk/
- Slack sandbox workspace: https://cupsafeslackdesk.slack.com/
- Local demo video asset: `media/cupsafe-slack-desk-demo.mp4`
- Local slash-command service: `python server/slack_endpoint.py` on `http://127.0.0.1:8787/slack/commands`
- Public HTTPS slash-command endpoint: `https://e2368d0f811bff63-218-85-208-206.serveousercontent.com/slack/commands`

## Current state

The hosted demo is a static, credential-free prototype. It demonstrates the
Slack-style incident triage flow and can be reviewed without installing a Slack
app.

A Slack app named `CupSafe Slack Desk` has been created and installed into the
`CupSafe Slack Desk` sandbox workspace. No Slack token is stored in this repo.

## Still pending

- Configure Slack `/cupsafe-check` with the public HTTPS tunnel URL.
- Judge access invite.
- Devpost country/region field.
- Devpost final submission.

## Low-risk endpoint path

- Use the local Python endpoint plus a free Serveo HTTPS reverse tunnel.
- This requires no wallet, payment, KYC, custom domain, or cloud account.
- The URL is temporary and changes when the tunnel process restarts.
- The endpoint remains available only while this computer, the Python service, and the SSH tunnel are running.
- Cloudflare TryCloudflare was skipped because local disk space was insufficient for downloading `cloudflared`.
