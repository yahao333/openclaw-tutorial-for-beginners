# 第四章：基础配置

## 配置文件介绍

OpenClaw 的配置文件位于 `~/.openclaw/openclaw.json`。你可以直接编辑这个 JSON 文件来配置 OpenClaw。

### 工作空间文件

除了配置文件，OpenClaw 还使用 workspace（工作目录）中的 Markdown 文件来定义 AI 的行为：

| 文件 | 作用 |
|------|------|
| `SOUL.md` | 定义 AI 的性格和风格 |
| `USER.md` | 关于你的信息 |
| `AGENTS.md` | 工作空间的规则 |
| `MEMORY.md` | 长期记忆 |

> **注意**：工作空间目录可以在配置文件中指定，默认在 `~/.openclaw/workspace/`

## 配置文件示例

`~/.openclaw/openclaw.json` 的基本配置：

```json
{
  "channels": {
    "whatsapp": {
      "allowFrom": ["+15555550123"]
    }
  },
  "messages": {
    "groupChat": {
      "mentionPatterns": ["@openclaw"]
    }
  }
}
```

### 常用配置项

- `channels` - 频道设置（如 WhatsApp、Telegram 的白名单）
- `messages` - 消息处理规则
- `gateway` - Gateway 相关设置（端口、模型等）

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

OpenClaw 使用"技能"(Skills)来扩展功能。你可以在 `~/.openclaw/skills/` 目录中添加新的技能。

## 本章小结

本章我们学习了 OpenClaw 的基础配置。在下一章中，我们将学习如何使用技能系统。
