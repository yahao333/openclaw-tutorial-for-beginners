---
name: devops
description: |
  DevOps 工具集，支持 Git 版本控制、CI/CD 流水线操作、代码提交推送等功能。
  当用户需要以下操作时触发：
  (1) Git 提交代码（git commit）
  (2) 推送代码到远程（git push/pull）
  (3) 创建和切换分支
  (4) 查看 Git 状态和历史
  (5) GitHub Actions 工作流操作
  (6) 部署相关操作
  (7) 构建和测试命令
---

# DevOps 工具集

## 快速开始

### Git 基础操作

```bash
# 查看状态
git status

# 查看历史
git log --oneline -10

# 添加文件
git add .

# 提交
git commit -m "描述"

# 推送到远程
git push origin <分支名>

# 拉取最新代码
git pull
```

### 分支操作

```bash
# 创建并切换分支
git checkout -b <分支名>

# 切换分支
git checkout <分支名>

# 删除本地分支
git branch -d <分支名>

# 删除远程分支
git push origin --delete <分支名>
```

### GitHub 操作

```bash
# 查看 PR 列表
gh pr list

# 创建 PR
gh pr create --title "标题" --body "描述"

# 查看 Actions 工作流
gh run list

# 触发工作流
gh workflow run <workflow-file>
```

## 常用工作流

### 提交代码标准流程

1. `git status` - 查看改动
2. `git diff` - 确认改动内容
3. `git add .` - 添加所有改动
4. `git commit -m "feat: 添加新功能"` - 提交（遵循 Conventional Commits）
5. `git push` - 推送到远程

### 代码审查流程

1. 创建功能分支
2. 开发完成后提交 PR
3. 使用 `gh pr review` 添加审查意见
4. 合并分支

## 提交规范

遵循 [Conventional Commits](https://www.conventionalcommits.org/)：

| 类型 | 说明 |
|------|------|
| `feat:` | 新功能 |
| `fix:` | Bug 修复 |
| `docs:` | 文档更新 |
| `style:` | 代码格式 |
| `refactor:` | 代码重构 |
| `test:` | 测试相关 |
| `chore:` | 构建/工具 |

## CI/CD 参考

### GitHub Actions 基础

```yaml
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: npm test
```

### 常用 Actions

- `actions/checkout@v4` - 检出代码
- `actions/setup-node@v4` - 设置 Node.js
- `aws-actions/configure-aws-credentials@v4` - AWS 配置

## 注意事项

- 危险操作前提示确认（如 `git push --force`、`git reset --hard`）
- 保护敏感信息（不提交 .env、密钥等）
- 大文件使用 Git LFS
