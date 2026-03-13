# 第六章：飞书集成

## 为什么需要飞书？

飞书是字节跳动推出的企业协作平台，OpenClaw 可以读取和操作你的飞书：

- 文档
- 任务
- 云盘文件
- 知识库
- 表格

> **注意**：飞书集成是 OpenClaw 内置功能，无需单独安装插件。

## 配置飞书

### 方法一：使用引导向导（推荐）

首次配置时，使用 onboard 命令：

```bash
openclaw channels add
```

选择 **Feishu**，输入你的 App ID 和 App Secret。

### 方法二：手动配置

#### 第一步：获取飞书应用凭证

1. 打开飞书开放平台：https://open.feishu.cn/
2. 创建企业自建应用
3. 获取 App ID 和 App Secret

#### 第二步：配置权限

在飞书开放平台的应用权限中，添加以下权限：

- `im:message` - 消息相关权限
- `im:message:send_as_bot` - 发送消息
- `im:resource` - 资源访问
- `aily:file:read` / `aily:file:write` - 文件读写

#### 第三步：配置 OpenClaw

在 `~/.openclaw/openclaw.json` 中添加飞书配置：

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "accounts": {
        "main": {
          "appId": "你的App ID",
          "appSecret": "你的App Secret",
          "botName": "My AI助手"
        }
      }
    }
  }
}
```

## 验证配置

配置完成后，检查 Gateway 状态：

```bash
openclaw gateway status
openclaw logs --follow
```

## 使用飞书功能

配置完成后，你可以让 OpenClaw 帮你：

- 读取飞书文档内容
- 创建和更新飞书任务
- 上传文件到飞书云盘
- 管理知识库
- 操作飞书表格

## 本章小结

本章我们学习了如何连接飞书。在下一章中，我们将学习如何开发自定义技能。
