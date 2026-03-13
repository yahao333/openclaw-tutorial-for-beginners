# 第十三章：数据库操作

## 概述

OpenClaw 可以连接各种数据库，执行查询和管理操作。

## 支持的数据库

- MySQL / MariaDB
- PostgreSQL
- MongoDB
- Redis
- SQLite

## MySQL/PostgreSQL

### 配置连接

```json
{
  "database": {
    "mysql": {
      "host": "localhost",
      "port": 3306,
      "user": "root",
      "password": "password",
      "database": "myapp"
    }
  }
}
```

### 使用示例

#### 查询数据

```
查询 users 表中最近注册的用户
```

#### 插入数据

```
在 orders 表中添加一条新订单
```

#### 更新数据

```
把用户张三的积分改成100
```

#### 删除数据

```
删除三个月前的临时数据
```

## MongoDB

### 配置连接

```json
{
  "database": {
    "mongodb": {
      "uri": "mongodb://localhost:27017",
      "database": "myapp"
    }
  }
}
```

### 使用示例

```
查找 products 集合中价格小于100的商品
```

## Redis

### 配置连接

```json
{
  "database": {
    "redis": {
      "host": "localhost",
      "port": 6379,
      "password": "",
      "db": 0
    }
  }
}
```

### 使用示例

#### 缓存管理

```
把用户配置缓存到 Redis，过期时间1小时
```

#### 计数器

```
统计网站今天的访问量
```

#### 消息队列

```
添加一个异步任务到队列
```

## 数据导出

### 导出为 CSV

```
把 orders 表导出为 CSV 文件
```

### 导出为 Excel

```
导出月度报表为 Excel
```

### 导出到飞书表格

```
把查询结果直接写入飞书 Bitable
```

## 自动化备份

### 定时备份

```markdown
HEARTBEAT.md 配置：
- 每天凌晨2点自动备份数据库
```

### 备份到云存储

```
备份文件自动上传到飞书云盘
```

## 本章小结

本章我们学习了数据库操作的基本用法。在下一章中，我们将学习文件自动化处理。

---

## 📖 导航

- [🏠 教程大纲](../README.md)
- [← 上一章](./12-ai-capabilities.md)
- [下一章 →](./14-file-automation.md)

---
