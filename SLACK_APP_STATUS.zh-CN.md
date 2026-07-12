# Slack app 状态

时间：2026-07-12 +08:00

## 已完成

- 已创建 Slack workspace：`CupSafe Slack Desk`
- Workspace URL：`https://cupsafeslackdesk.slack.com/`
- 已创建 Slack app：`CupSafe Slack Desk`
- App ID：`A0BGQ5542RF`
- 已安装到 `CupSafe Slack Desk` workspace
- 已配置 slash command：`/cupsafe-check`
- 已配置权限：`commands`、`chat:write`、`channels:read`、`groups:read`
- 已启动本地 demo endpoint：`http://127.0.0.1:8787/slack/commands`
- 已启动临时 HTTPS 隧道：`https://e2368d0f811bff63-218-85-208-206.serveousercontent.com/slack/commands`
- 已验证公网 endpoint：`/health` 和 `/slack/commands` 均返回 HTTP 200。

## 未完成

- Slack app 管理后台当前需要人工清理 `/cupsafe-check` Request URL：自动填写时把 endpoint 拼接了两次。请把该字段完整替换为单个 `https://e2368d0f811bff63-218-85-208-206.serveousercontent.com/slack/commands` 后保存。
- 临时 HTTPS endpoint 依赖当前电脑、本地 Python 服务和 SSH 隧道持续运行；重启后 URL 可能变化。
- 还没有邀请官方评审账号。
- Devpost 草稿已保存 Project overview 和 Project details；Additional info 已填写可确定字段。
- Devpost Additional info 中架构图已由用户上传；用户已表示国家选择日本，日本在 Devpost 页面列出的允许范围内。保存 Additional info 后可进入 finalization。

## 安全记录

- 没有保存 Slack bot token、signing secret、verification token 或浏览器密码。
- 没有读取私钥、助记词、钱包文件或桌面 `14usdt.txt`。
- 没有付费、KYC、钱包连接、签名、交易或转账。
