# 第五章：技能使用

## 什么是技能？

技能（Skills）是 OpenClaw 的扩展功能，每个技能可以给 AI 添加新的能力，比如：

- 查天气
- 操作飞书
- 管理 GitHub
- 定时提醒

## 查看内置技能

### 方法一：使用 CLI 命令

```bash
# 查看所有已安装的技能
openclaw skills list
```

### 方法二：查看技能目录

内置技能保存在 `~/.openclaw/skills/` 目录中：

```bash
ls ~/.openclaw/skills/
```

### 方法三：在控制面板查看

Gateway 启动后，访问控制面板 http://127.0.0.1:18789/ 可以查看已安装的技能列表。

## 常用内置技能

### 天气技能
```
深圳天气怎么样？
```

### 飞书技能
- 读取飞书文档
- 创建飞书任务
- 管理飞书云盘

### GitHub 技能
- 创建仓库
- 查看 issues
- 管理 PR

## 安装新技能

你可以通过 ClawHub 安装更多技能：

```bash
# 搜索技能
clawhub search <关键词>

# 安装技能
clawhub install <技能名>
```

## 本章小结

本章我们学习了技能的基本使用方法。在下一章中，我们将学习如何连接飞书。

---

## 📖 导航

- [🏠 教程大纲](../README.md)
- [← 上一章](./04-basic-configuration.md)
- [下一章 →](./06-feishu-integration.md)

---
