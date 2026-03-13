# 第三章：初次运行

## 启动 OpenClaw

安装完成后，在终端中输入以下命令启动 OpenClaw：

```bash
# 初始化安装服务（首次运行）
openclaw onboard --install-daemon

# 启动 Gateway
openclaw gateway --port 18789
```

> **提示**：如果不指定端口，默认使用 `18789`。

## 初始设置

第一次运行时，OpenClaw 会引导你完成基本设置。`openclaw onboard` 命令会帮助你：

### 1. 安装服务守护进程

使用 `--install-daemon` 可以在系统启动时自动运行 OpenClaw。

### 2. 连接通讯渠道

你可以让 OpenClaw 通过多种渠道与你沟通：

```bash
# 登录并配置频道
openclaw channels login
```

支持的渠道包括：
- **网页聊天** - 通过浏览器直接聊天
- **飞书** - 绑定飞书账号
- **Telegram** - 绑定 Telegram Bot
- **WhatsApp** - 绑定 WhatsApp 账号
- **Discord** - 绑定 Discord Bot

### 3. 打开控制面板

Gateway 启动后，可以通过浏览器访问控制面板：

- 本地地址：http://127.0.0.1:18789/

在这里你可以：
- 与 AI 聊天
- 查看和管理会话
- 配置频道和节点
- 查看日志

## 恭喜入门！

完成初始设置后，你就可以开始使用 OpenClaw 了。试着和它聊聊天吧！

## 本章小结

本章我们完成了 OpenClaw 的首次运行和基本配置。在下一章中，我们将学习如何进一步配置 OpenClaw。
