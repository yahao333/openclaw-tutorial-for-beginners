---
name: digital-twin
description: 建立数字分身 - 从 Twitter 爬取用户推文进行分析，提取写作风格、常用词汇、观点倾向等特征
author: yanghao
version: 1.0.0
metadata:
  openclaw:
    categories: [ai, profile, social-media]
    tags: [digital-twin, twitter, analysis, 数字分身, 推文分析]
    user-invocable: true
---

# 数字分身建立技能

## 概述

本技能用于从 Twitter 爬取用户的推文内容，进行分析和建模，建立用户的数字分身。

## 触发条件

当用户消息中出现以下关键词时触发：
- 建立数字分身
- 分析 Twitter
- 爬取推文
- 数字人
- 分析我的风格

## 执行步骤

### 1. 获取 Twitter 用户信息

首先需要知道用户的 Twitter 用户名（Handle）。

如果用户没有提供，需要询问：
- 请问你的 Twitter 用户名是什么？（不带 @）

### 2. 选择爬取方式

**方式一：使用浏览器手动查看（推荐）**
- 打开 Twitter 用户主页
- 滚动加载更多推文
- 截图或复制推文内容

**方式二：使用 Twitter API（如有权限）**
```bash
# 需要 Twitter Developer 账号和 API Key
curl "https://api.twitter.com/2/users/{id}/tweets"
```

**方式三：使用 web_fetch 或 browser 工具**
- 使用 browser 打开用户主页
- 使用 web_fetch 获取页面内容

### 3. 分析推文内容

分析以下维度：
- **写作风格**：正式/随意/幽默/严肃
- **常用词汇**：高频词汇和短语
- **主题领域**：技术/生活/商业/政治等
- **情感倾向**：积极/消极/中性
- **发布习惯**：时间/频率/互动方式
- **观点倾向**：保守/激进/中立

### 4. 生成分析报告

输出格式：
```
📊 Twitter 数字分身分析报告

👤 用户：@xxx

📝 写作风格：
- 总体风格：xxx
- 语气：xxx
- 句式特点：xxx

📚 常用词汇/主题：
- 高频词1
- 高频词2
- ...

💭 观点倾向：
- 主要领域：xxx
- 倾向性：xxx

📅 发布习惯：
- 活跃时间：xxx
- 平均频率：xxx

🎯 总结：
[一段描述用户社交媒体形象的文字]
```

## 注意事项

- Twitter 可能有反爬虫机制，需谨慎使用
- 确保遵守 Twitter 的使用条款
- 保护用户隐私，不要存储敏感信息

## 输出文件

分析完成后，可以将结果保存为：
- `~/.openclaw/workspace/digital-twin/{username}-analysis.md`
- 或保存到飞书文档
