# Slack app 设置 runbook

## 目标

把 `CupSafe Slack Desk` 从本地演示推进到可提交状态。当前文件只是操作清单；我没有创建、授权或读取任何 Slack token。

## 需要用户确认后才能执行

1. 允许创建或使用一个 Slack workspace / developer sandbox。
2. 允许创建 Slack app。
3. 允许配置 slash command 或 message shortcut。
4. 允许生成并保存部署所需的非敏感配置。
5. 允许给官方评审账号开放 sandbox 访问。

## 建议设置

- App name: `CupSafe Slack Desk`
- Slash command: `/cupsafe-check`
- Short description: `Explain wallet-risk incidents before a user signs.`
- Long description: `CupSafe Slack Desk triages wallet support incidents, matches prior scam memory, and returns ALLOW, REVIEW, or DENY with evidence.`

## Manifest 草稿

使用：

`slack/app-manifest.example.json`

注意：manifest 里的 request URL 目前是占位符。只有在用户确认托管 endpoint 后才能填写真实地址。

## 最小测试流程

1. 在 Slack sandbox 里安装 app。
2. 创建 `#cupsafe-demo` 频道。
3. 用 `/cupsafe-check` 输入一个合成事件，例如：

   `User says support DM asked them to approve unlimited USDT spending before help.`

4. 预期输出：

   - Decision: `DENY`
   - Severity: `critical`
   - Evidence: prior support-impersonation / approval memory
   - Next action: do not sign, revoke/reduce allowance

## 不要做

- 不把真实用户钱包地址、私钥、助记词或交易签名传入 Slack。
- 不读取 Slack token 或浏览器密码库。
- 不在没有用户确认时邀请评审、提交 Devpost 或发布视频。
