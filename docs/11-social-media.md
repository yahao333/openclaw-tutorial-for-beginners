# 第十一章：社交媒体集成

## 概述

OpenClaw 可以连接各种社交媒体平台，帮你管理社交账号。

## 支持的平台

- Twitter / X
- Discord
- Slack
- Telegram
- WhatsApp

## Discord 集成

### 配置步骤

1. 创建 Discord Bot
2. 获取 Bot Token
3. 配置到 OpenClaw

```json
{
  "discord": {
    "bot_token": "your-bot-token",
    "channels": ["general", "notifications"]
  }
}
```

### 功能

- 自动回复消息
- 定时发送更新
- 监听特定关键词
- 管理频道

## Slack 集成

### 配置步骤

1. 创建 Slack App
2. 添加 Bot Token
3. 配置权限范围

```json
{
  "slack": {
    "bot_token": "xoxb-...",
    "signing_secret": "...",
    "app_token": "xapp-..."
  }
}
```

### 功能

- 发送消息到频道
- 响应 slash 命令
- 处理 events
- 创建 workflow

## Twitter/X 集成

### 配置步骤

1. 创建 Twitter Developer 账号
2. 创建 App 获取 API Keys
3. 配置 OAuth 访问

```json
{
  "twitter": {
    "api_key": "...",
    "api_secret": "...",
    "access_token": "...",
    "access_token_secret": "..."
  }
}
```

### 功能

- 发推文
- 读取时间线
- 搜索推文
- 自动化发帖

## Telegram 集成

### 配置步骤

1. @BotFather 创建机器人
2. 获取 HTTP API Token
3. 配置到 OpenClaw

```json
{
  "telegram": {
    "bot_token": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
  }
}
```

### 功能

- 群组管理
- 自动回复
- 文件传输
- 投票功能

## 自动化示例

### 跨平台同步

```
当 Discord 发布新消息时，自动转发到 Telegram 群
```

### 定时发布

```
每天早上9点自动同步状态到所有社交平台
```

### 关键词监控

```
当 Twitter 有人提到你的产品时，发送通知到 Discord
```

## 本章小结

本章我们学习了各种社交媒体的集成方法。在下一章中，我们将学习 AI 能力集成。
