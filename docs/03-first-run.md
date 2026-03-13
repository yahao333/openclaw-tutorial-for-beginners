# 第三章：初次运行

## 初始化 OpenClaw

首次使用 OpenClaw，需要先初始化并安装服务：

```bash
# 初始化安装服务（首次运行推荐）
openclaw onboard --install-daemon
```

`openclaw onboard` 会引导你完成：
- 创建飞书应用并获取凭证
- 配置应用凭证
- 启动 Gateway

## 启动 Gateway

初始化完成后，使用以下命令启动 Gateway：

```bash
# 启动 Gateway（默认端口 18789）
openclaw gateway --port 18789

# 或者直接运行（使用默认端口）
openclaw gateway
```

## 配置频道

如果你想添加或修改通讯渠道：

```bash
# 登录并配置频道
openclaw channels login
```

支持的频道：
- **网页聊天** - 通过浏览器直接聊天
- **飞书** - 绑定飞书账号
- **Telegram** - 绑定 Telegram Bot
- **WhatsApp** - 绑定 WhatsApp 账号
- **Discord** - 绑定 Discord Bot
- **iMessage** - macOS 上的 iMessage

## 控制面板

Gateway 启动后，通过浏览器访问控制面板：

- 本地地址：http://127.0.0.1:18789/

在控制面板中可以：
- 与 AI 聊天
- 查看和管理会话
- 配置频道和节点
- 查看日志

## 恭喜入门！

完成初始设置后，你就可以开始使用 OpenClaw 了。试着和它聊聊天吧！

## 本章小结

本章我们完成了 OpenClaw 的首次运行和基本配置。在下一章中，我们将学习如何进一步配置 OpenClaw。

---

## 📖 导航

- [🏠 教程大纲](../README.md)
- [← 上一章](./02-environment-setup.md)
- [下一章 →](./04-basic-configuration.md)

---
