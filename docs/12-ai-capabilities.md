# 第十二章：AI 能力集成

## 概述

OpenClaw 可以集成各种 AI 服务，让你的 AI 助手更强大。

## 图像生成

### DALL-E 集成

让 AI 生成图片：

```
帮我生成一张科技感的桌面壁纸
```

生成的图片可以直接发送给用户或保存到云盘。

### Midjourney 集成

通过 API 调用 Midjourney：

```
生成一张赛博朋克风格的城市图片
```

## 语音合成（TTS）

### 功能

将文字转换为语音：

- 支持多种声音
- 支持多种语言
- 可调节语速和音调

### 使用示例

```
用语音给我讲个故事
把这段文章朗读出来
```

### 配置声音

```json
{
  "tts": {
    "provider": "elevenlabs",
    "voice": "rachel",
    "stability": 0.5,
    "similarity_boost": 0.75
  }
}
```

## 语音识别（STT）

### 功能

将语音转换为文字：

- 实时语音转写
- 会议记录
- 语音笔记转文字

### 使用示例

```
帮我转写这段录音
```

## AI 绘图编辑

### 功能

- 图片修复（inpainting）
- 图片扩展（outpainting）
- 风格转换
- 去除背景

### 使用示例

```
把这张照片的背景去掉
把图片中的汽车换成自行车
```

## 大语言模型

### 自定义模型

可以配置使用不同的 AI 模型：

```json
{
  "model": {
    "provider": "openai",
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 2000
  }
}
```

### 支持的模型

- OpenAI GPT-4 / GPT-3.5
- Anthropic Claude
- Google Gemini
- 本地模型（Llama 等）

### 使用场景

- 更专业的问答
- 代码生成
- 长文本处理
- 私有化部署

## 向量数据库

### 功能

存储和检索 embeddings：

- 知识库问答
- 语义搜索
- 相似度匹配

### 使用示例

```
在我自己的知识库里搜索"OpenClaw 安装"
```

## 本章小结

本章我们学习了各种 AI 能力的集成方法。在下一章中，我们将学习数据库操作。

---

## 📖 导航

- [🏠 教程大纲](../README.md)
- [← 上一章](./11-social-media.md)
- [下一章 →](./13-database-operations.md)

---
