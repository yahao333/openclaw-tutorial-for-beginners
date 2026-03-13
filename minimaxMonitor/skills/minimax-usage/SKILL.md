---
name: minimax-usage
description: 查询 MiniMax 账号当前使用量和剩余额度
author: yanghao
version: 1.0.0
metadata:
  openclaw:
    categories: [utility, monitor]
    tags: [minimax, usage, quota, 额度, 使用量]
    user-invocable: true
---

## 触发条件

当用户消息中出现以下关键词时触发：
- MiniMax 使用量
- minimax 剩余
- API 额度
- 还有多少额度
- 使用量查询
- 剩余百分之几

## 执行规则

1. **获取当前会话使用量**：
   - 调用 session_status 获取当前会话的 token 使用量和费用
   - 解析返回的 usage 信息

2. **账户总体使用量**：
   - MiniMax API 目前没有提供直接查询账户总余额的公开接口
   - 需要用户登录 MiniMax 控制台查看：https://platform.minimaxi.com/accountcenter

3. **输出格式**：
   - 显示当前会话的使用量
   - 提供 MiniMax 控制台链接供用户查看总体额度

## 输出示例

```
🤖 MiniMax 使用量查询

📊 当前会话：
- 输入 Tokens: xxx
- 输出 Tokens: xxx
- 费用: $xxx
- 上下文使用: xxx/200k (xx%)

💡 账户总体额度请访问：
   https://platform.minimaxi.com/accountcenter
```

## 备注

- 当前仅支持查询当前会话的使用量统计
- 账户总体额度需要在 MiniMax 官网查看
- 如需长期监控，可结合 subagent 定期调用此 skill
