# OpenClaw 工具使用教程参考

## 核心工具

### 文件操作
- **read**: 读取文件内容
- **write**: 创建或覆盖文件
- **edit**: 精确编辑文件

### 执行命令
- **exec**: 运行 shell 命令
- **process**: 管理后台进程

### 浏览器控制
- **browser**: 控制浏览器自动化
- **web_fetch**: 获取网页内容
- **web_search**: 搜索网页

### 消息通讯
- **message**: 发送消息到各种平台
- **sessions**: 管理会话和子代理

## 飞书集成工具

- **feishu_doc**: 文档操作
- **feishu_drive**: 云盘操作
- **feishu_wiki**: 知识库操作
- **feishu_task**: 任务管理
- **feishu_bitable**: 多维表格

## 节点控制

- **nodes**: 控制配对的设备
- **camera_snap**: 拍照
- **screen_record**: 录屏

## 常用工作流

### 1. 创建新 Skill
```bash
mkdir -p ~/.openclaw/workspace/skills/<name>
# 编写 SKILL.md
```

### 2. 浏览器自动化
```bash
browser(action=open, url="...")
browser(action=snapshot)
browser(action=act, request={...})
```

### 3. 文件处理
```bash
read(file_path="...")
write(content="...", path="...")
edit(path="...", old_string="...", new_string="...")
```
