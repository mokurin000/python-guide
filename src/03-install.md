# 安装环境

在开始之前，我们需要先安装 CPython 与开发环境。

- [CPython 3.14.6](https://mirrors.bfsu.edu.cn/python/3.14.6/)
- [Visual Studio Code](https://code.visualstudio.com/Download)
  - Ruff
  - Even Better TOML
  - Pylance
  - Rainbow CSV

注意，你的 Windows 版本应该不低于 Windows 10 。

此处安装过程以 Windows x86_64 为例，桌面 Linux/Termux 用户可通过相关社群寻求帮助。

## Python 本体

### 下载安装器

通过[该链接](https://mirrors.bfsu.edu.cn/python/3.14.6/python-3.14.6-amd64.exe)下载 Python 安装包。

### 启动安装器

![Python安装器](img/03/step01.png)

点击 **Customize Installation**

### 调整选项

![调整选项](img/03/step02.png)

取消勾选 `py launcher` 和 `for all users` 后，点击 **Next**

### 高级选项

![高级选项](img/03/step03.png)

勾选 `Precompile standard library`, 点击 **Install**

### 安装完成

等待数分钟后，如果一切正常，你就会进入如下界面:

![安装完成](img/03/step04.png)

点击 `Disable path length limit`, 同意授权，然后点击 `Close` 关闭即可。

## Visual Studio Code

**WIP: VSCode v.s. PyCharm**
