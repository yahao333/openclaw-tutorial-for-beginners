# 第七章：自定义技能

## 创建自己的技能

当你现有的技能不能满足需求时，可以自己动手创建新技能。

## 技能目录结构

一个技能通常包含以下文件：

```
my-custom-skill/
├── SKILL.md          # 技能说明文件
├── handler.js        # 处理逻辑
└── config.json       # 配置文件（可选）
```

## 技能文件说明

### SKILL.md

这是技能的核心文件，格式如下：

```markdown
# SKILL.md

## 描述
简要说明这个技能是做什么的

## 触发条件
当用户说 XXX 时使用此技能

## 使用方法
- 命令1：做 XXX
- 命令2：做 YYY
```

### handler.js

处理用户请求的代码：

```javascript
module.exports = {
  // 技能名称
  name: 'my-skill',
  
  // 处理函数
  async handle(context) {
    const input = context.input;
    // 处理逻辑
    return '处理结果';
  }
};
```

## 安装技能

创建完成后，把技能文件夹复制到 `~/.openclaw/skills/` 目录即可。

## 本章小结

本章我们学习了如何创建自定义技能。在最后一章中，我们将介绍一些高级主题。

---

## 📖 导航

- [🏠 教程大纲](../README.md)
- [← 上一章](./06-feishu-integration.md)
- [下一章 →](./08-advanced-topics.md)

---
