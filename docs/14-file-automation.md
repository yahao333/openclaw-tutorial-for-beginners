# 第十四章：文件自动化处理

## 概述

OpenClaw 可以帮你自动化处理各种文件，包括 PDF、Excel、图片等。

## PDF 处理

### 功能

- PDF 读取和提取文本
- PDF 合并和拆分
- PDF 转换为图片
- 添加水印

### 使用示例

```
提取这份 PDF 报告的所有文字
把这两个 PDF 合并成一个
```

### 代码示例

```javascript
// PDF 提取
const pdf = await openclaw.extractPDF('report.pdf');
console.log(pdf.text);
```

## Excel/CSV 处理

### 功能

- 读取和写入 Excel
- 数据分析
- 公式计算
- 多sheet管理

### 使用示例

```
分析这份销售数据报表
计算每个月的总收入
```

### 代码示例

```javascript
// 读取 Excel
const data = await openclaw.readExcel('sales.xlsx');
// 计算总和
const total = data.reduce((sum, row) => sum + row.amount, 0);
```

## 图片处理

### 功能

- 缩放和裁剪
- 格式转换
- 添加水印
- OCR 文字识别

### 使用示例

```
识别这张图片中的文字
把图片转换成 PNG 格式
压缩这个图片文件
```

### OCR 示例

```
从截图提取订单号
扫描文档识别为文字
```

## 文档格式转换

### 支持的转换

- Word → PDF
- Markdown → Word
- HTML → PDF
- 图片 → PDF

### 使用示例

```
把这份 Markdown 文档转成 PDF
把 Word 文档转成 Markdown
```

## 压缩和解压

### 功能

- ZIP 压缩和解压
- TAR/GZ 处理
- 7z 支持

### 使用示例

```
解压这个 zip 文件
把整个文件夹压缩备份
```

## 文件监控

### 功能

- 监控文件夹变化
- 自动处理新文件
- 触发条件执行任务

### 使用示例

```
当 downloads 文件夹有新文件时，自动压缩并发送到云盘
```

## 云盘同步

### 功能

- 本地文件同步到云盘
- 云盘文件同步到本地
- 双向同步

### 支持的云存储

- 飞书云盘
- Google Drive
- Dropbox
- S3 / OSS

### 使用示例

```
把本地项目文件夹同步到飞书云盘
```

## 自动化工作流

### 示例 1：文档处理流水线

```
1. 监控文件夹收到新 PDF
2. 提取 PDF 文字
3. 发送到邮箱
4. 移动到已处理文件夹
```

### 示例 2：数据处理流水线

```
1. 每天早上下载Excel报表
2. 分析数据生成汇总
3. 发送到钉钉群
4. 备份原始文件
```

## 本章小结

本章我们学习了各种文件处理的能力。现在你已经掌握了 OpenClaw 的完整功能！

## 下一步

- 访问官方文档：https://docs.openclaw.ai
- 加入社区：https://discord.com/invite/clawd
- 发现更多技能：https://clawhub.com

祝你使用愉快！🎉

---

## 📖 导航

- [🏠 教程大纲](../README.md)
- [← 上一章](./13-database-operations.md)


---
