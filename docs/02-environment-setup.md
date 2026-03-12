# 第二章：环境准备

## 准备工作

在开始使用 OpenClaw 之前，你需要准备以下环境：

## 1. 安装 Node.js

OpenClaw 基于 Node.js 运行，请确保你的电脑上安装了 Node.js。

### Windows 和 macOS 用户

1. 访问 Node.js 官网：https://nodejs.org
2. 下载 LTS（长期支持）版本
3. 运行安装程序，按照提示完成安装

### macOS 用户（推荐使用 Homebrew）

```bash
# 安装 Homebrew（如果没有的话）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装 Node.js
brew install node
```

### Linux 用户

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nodejs npm

# CentOS/RHEL
sudo yum install nodejs npm
```

## 2. 验证安装

打开终端（Windows 用户使用 PowerShell 或 CMD），输入以下命令：

```bash
node --version
npm --version
```

如果看到版本号，说明安装成功。

## 3. 安装 OpenClaw

使用 npm 全局安装 OpenClaw：

```bash
npm install -g openclaw
```

## 本章小结

本章我们完成了环境准备。现在你应该已经安装了 Node.js 和 OpenClaw。在下一章中，我们将学习如何首次运行 OpenClaw。
