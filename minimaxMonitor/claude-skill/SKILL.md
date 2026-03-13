---
name: minimax-usage
version: "1.0.0"
description: 查看 MiniMax 账号当前使用量和余额。通过浏览器自动登录 MiniMax 平台并导航到账户页面查看使用量信息。
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - WebFetch
  - WebSearch
  - Browser
---

# MiniMax 使用量查询技能

用于查询 MiniMax 账号的当前使用量和余额信息。

## 使用方法

当用户说以下关键词时触发：
- "MiniMax 使用量"
- "minimax 剩余"
- "查看余额"
- "还有多少额度"
- "使用量查询"

## 执行步骤

### 1. 启动浏览器

使用 Browser 工具启动浏览器。

### 2. 打开 MiniMax 登录页面

访问: https://platform.minimaxi.com/login

### 3. 登录（需要用户配合）

- 如果未登录，引导用户完成手机验证码登录
- 输入手机号 → 获取验证码 → 输入验证码 → 勾选协议 → 登录

### 4. 导航到账户页面

登录成功后，导航到以下任一页面查看使用量：
- 账户信息: https://platform.minimaxi.com/user-center/basic-information
- 余额页面: https://platform.minimaxi.com/user-center/balance
- 套餐管理: https://platform.minimaxi.com/user-center/subscription

### 5. 截图并提取信息

- 截图保存使用量页面
- 提取关键信息：余额、已使用量、剩余百分比等
- 将信息返回给用户

## 注意事项

- MiniMax API 暂未开放余额查询接口，必须通过浏览器查看
- 每次查询需要用户登录配合（验证码）
- 可以使用 OpenClaw 的 Browser 工具进行自动化操作

## 输出格式

查询成功后，返回以下格式的信息：

```
🤖 MiniMax 使用量查询结果

📊 账户信息：
- 邮箱：xxx
- GroupID：xxx

💰 余额/使用量：
- [从页面提取的具体信息]

📅 查询时间：xxx
```

## 常见问题

### Q: 如何自动登录？
A: 目前需要用户手动输入验证码。未来可以尝试保存 Cookie 来实现自动登录。

### Q: 可以定期自动查询吗？
A: 可以通过配置 cron job 或 heartbeat 定期调用此技能，但需要解决登录问题。

### Q: 为什么不能通过 API 查询？
A: MiniMax 开放平台目前未提供查询账户余额的公开 API 接口。
