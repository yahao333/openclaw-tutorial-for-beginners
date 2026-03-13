# MiniMax Monitor

用于监控 MiniMax 账号使用量的项目。

## 项目结构

```
minimaxMonitor/
├── skills/
│   └── minimax-usage/
│       └── SKILL.md          # 查询使用量的 Skill
├── README.md
└── monitor.sh                # 监控脚本（可选）
```

## 使用方法

### 方式一：直接查询（当前会话使用量）

在对话中直接说：
- "查看使用量"
- "还有多少额度"
- "MiniMax 使用量"

系统会返回当前会话的 token 使用量信息。

### 方式二：Subagent 定期监控

可以通过创建 subagent 来定期检查使用量：

```bash
# 在 OpenClaw 中创建定时任务或使用 heartbeat
```

## 限制说明

- **当前会话使用量**：可正常查询
- **账户总余额**：MiniMax API 暂未开放，需手动访问 https://platform.minimaxi.com/accountcenter 查看

## 安装 Skill

将 `skills/minimax-usage` 目录复制到 `~/.openclaw/skills/` 即可：

```bash
cp -r ~/.openclaw/workspace/minimaxMonitor/skills/minimax-usage ~/.openclaw/skills/
```
