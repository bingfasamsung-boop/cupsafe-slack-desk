# Slack Demo Transcripts

## Flow 1 - Unknown Approval

**Mina in #wallet-support:** A user wants to approve 50 USDT for a contract linked from a Telegram DM. They say it is for a tournament reward claim.

**CupSafe Desk:** DENY. Unknown approval requests can expose token allowance after one signature. Tell the user not to sign and verify the contract from official project channels.

**Escalation:** Send the incident to #security-triage with the original message and the suspected reward-claim link.

## Flow 2 - Verified Merchant

**Kai in #payments-ops:** Verified fan shop checkout for 8 USDT. Recipient is known and the user has no other spending today.

**CupSafe Desk:** ALLOW. The payment is under the daily cap and matches a known merchant pattern. Ask the user to confirm the checkout domain before signing.

## Flow 3 - Bridge Review

**Nora in #security-triage:** User is bridging 12 USDT to a new chain before a live match. Route is known, but finality and destination chain are not confirmed.

**CupSafe Desk:** REVIEW. Bridge actions need destination-chain, address, route, and finality confirmation before the user signs.
