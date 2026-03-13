# 第六章：飞书集成

## 为什么需要飞书？

飞书是字节跳动推出的企业协作平台，OpenClaw 可以读取和操作你的飞书：

- 文档
- 任务
- 云盘文件
- 知识库

## 配置飞书

### 第一步：获取飞书应用凭证

1. 打开飞书开放平台：https://open.feishu.cn/
2. 创建企业自建应用
3. 获取 App ID 和 App Secret

### 第二步：配置 OpenClaw

在 workspace 目录创建 `feishu-config.json`：

```json
{
  "app_id": "你的App ID",
  "app_secret": "你的App Secret"
}
```

### 第三步：启用飞书技能

OpenClaw 会自动检测配置文件并启用飞书功能。

## 使用飞书功能

配置完成后，你可以让 OpenClaw 帮你：

- 读取飞书文档内容
- 创建和更新飞书任务
- 上传文件到飞书云盘
- 管理知识库

## 本章小结

本章我们学习了如何连接飞书。在下一章中，我们将学习如何开发自定义技能。

---

## 📖 导航

- [🏠 教程大纲](../README.md)
- [← 上一章](./05-using-skills.md)
- [下一章 →](./07-custom-skills.md)

---
