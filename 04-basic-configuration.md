# 第四章：基础配置

## 配置文件介绍

OpenClaw 使用两种配置文件：

### 主配置文件

主配置文件位于 `~/.openclaw/openclaw.json`，用于配置：

- 频道设置（飞书、Telegram、WhatsApp 等）
- 消息处理规则
- Gateway 相关设置（端口、模型等）

示例：

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "accounts": {
        "main": {
          "appId": "你的App ID",
          "appSecret": "你的App Secret"
        }
      }
    }
  },
  "messages": {
    "groupChat": {
      "mentionPatterns": ["@openclaw"]
    }
  }
}
```

### 工作空间文件

工作空间目录（默认 `~/.openclaw/workspace/`）中的 Markdown 文件用于定义 AI 的行为：

| 文件 | 作用 |
|------|------|
| `SOUL.md` | 定义 AI 的性格和风格 |
| `USER.md` | 关于你的信息 |
| `AGENTS.md` | 工作空间的规则 |
| `MEMORY.md` | 长期记忆 |

## 修改 AI 性格

打开工作空间中的 `SOUL.md` 文件，你可以修改 AI 的：

- 名字
- 说话风格
- 核心准则

例如：

```markdown
# SOUL.md - 你是谁

## 核心准则
- 直接了当，不说废话
- 有自己的观点，不盲目迎合

## 风格
- 简洁高效
- 偶尔带点幽默
```

## 设置个人信息

在工作空间的 `USER.md` 中填写你的信息：

```markdown
# USER.md - 关于你

- 名字：张三
- 称呼：老板
- 时区：北京时间
- 备注：喜欢技术，喜欢折腾
```

## 技能配置

OpenClaw 使用"技能"(Skills) 来扩展功能。你可以在 `~/.openclaw/skills/` 目录中添加新的技能。

## 本章小结

本章我们学习了 OpenClaw 的基础配置。在下一章中，我们将学习如何使用技能系统。

---

## 📖 导航

- [🏠 教程大纲](../README.md)
- [← 上一章](./03-first-run.md)
- [下一章 →](./05-using-skills.md)

---
