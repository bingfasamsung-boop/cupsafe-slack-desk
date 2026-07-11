# Slack 评审访问计划

## Devpost/Slack 可能需要的内容

根据当前提交要求，需要准备：

- Slack developer sandbox URL
- 评审可访问的 Slack app 或 demo workspace
- Demo video
- Architecture diagram
- Source code / repo
- Setup instructions

## 建议给评审的访问方式

1. 创建只用于 hackathon 的 Slack sandbox。
2. 创建频道：`#cupsafe-demo`。
3. 安装 `CupSafe Slack Desk` app。
4. 邀请官方评审邮箱或官方指定账号。
5. 固定一条说明消息，包含：
   - app 用途
   - `/cupsafe-check` 示例输入
   - 4 个测试案例
   - source/demo/video 链接

## 示例固定消息

```text
Welcome to the CupSafe Slack Desk judge sandbox.

Try:
/cupsafe-check User says support DM asked them to approve unlimited USDT spending before help.

Expected result:
DENY / critical, with prior scam-memory evidence and a safe support reply.

Other scenarios:
- verified merchant checkout -> ALLOW
- bridge with fresh contract -> REVIEW
- high slippage DEX route -> REVIEW
```

## 当前阻塞

这些都是账号动作，必须等用户确认：

- 创建/授权 Slack app
- 邀请评审
- 填写真实 sandbox URL
- 提交 Devpost
