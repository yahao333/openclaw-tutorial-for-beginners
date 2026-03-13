# Skill 开发教程参考

## 什么是 Skill？

Skill 是扩展 OpenClaw 能力的模块化包，通过 SKILL.md 文件为 LLM 提供专业知识和工作流程。

## Skill 目录结构

```
skill-name/
├── SKILL.md (必需)
│   ├── YAML frontmatter (name + description)
│   └── Markdown 指令
├── scripts/ (可选) - 可执行代码
├── references/ (可选) - 参考文档
└── assets/ (可选) - 资源文件
```

## SKILL.md 编写规范

### Frontmatter

```yaml
---
name: skill_name
description: Skill 描述，说明何时触发这个 Skill
---
```

### Body

- 使用简洁的语言
- 提供具体示例
- 说明工具使用方式

## 创建 Skill 步骤

1. 创建目录：`mkdir -p ~/.openclaw/workspace/skills/<skill-name>`
2. 编写 SKILL.md
3. 添加需要的资源文件
4. 重启 Gateway 或让 Agent 刷新 Skills

## 最佳实践

- **简洁优先**：只包含 LLM 需要的信息
- **适度自由**：根据任务复杂度决定指令详细程度
- **模块化**：长内容拆分到 references 文件
