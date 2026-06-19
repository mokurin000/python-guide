# 附录：第三方包与虚拟环境

在前两章中，我们学习了如何使用 Python 标准库和创建自己的包。但 Python 生态最强大的地方在于海量的**第三方包 (Third-party Packages)**——由全球开发者贡献的、可直接复用的代码库。

本附录将介绍如何安装第三方包、管理项目依赖，以及使用虚拟环境隔离不同项目的依赖。

## 安装第三方包

### PyPI —— Python 包索引

PyPI（Python Package Index，https://pypi.org/）是 Python 的官方第三方包仓库。几乎所有的开源 Python 包都发布在这里。

热门第三方包举例：

- `requests` —— 简洁的 HTTP 请求库
- `numpy` —— 科学计算基础库
- `flask` —— 轻量级 Web 框架
- `pandas` —— 数据分析库

### 使用 `uv` 安装包

```bash
# 安装一个包
$ uv add requests

# 安装特定版本
$ uv add "requests>=2.28,<3"

# 一次性安装多个包
$ uv add numpy pandas matplotlib
```

`uv add` 会：

1. 下载并安装指定包（及其依赖）
2. 将包信息记录到 `pyproject.toml` 的 `dependencies` 列表中
3. 更新锁定文件，确保可重复安装

### 从 `requirements.txt` 安装

一些项目仍使用传统的 `requirements.txt` 记录依赖：

```bash
$ uv pip install -r requirements.txt
```

> `uv pip install` 兼容 `pip install` 的用法，可以作为 `pip` 的**替代品**。建议优先使用 `uv add` 来管理依赖。

## 虚拟环境

### 为什么要虚拟环境？

假设你有两个项目：

- 项目 A 需要 `requests 2.28`
- 项目 B 需要 `requests 2.31`

如果所有包都安装到全局的 Python 环境中，就会出现冲突——这就是**依赖地狱 (Dependency Hell)**。

**虚拟环境 (Virtual Environment)** 为每个项目创建独立的 Python 环境，各自拥有独立的 `site-packages` 目录。每个项目可以安装不同版本的依赖，互不干扰。

### 使用 `uv venv` 创建虚拟环境

```bash
# 在项目目录中创建虚拟环境
$ uv venv

# 指定 Python 版本
$ uv venv --python 3.12
```

执行后会在当前目录下创建 `.venv` 文件夹，其中包含一个独立的 Python 解释器和包安装目录。

### 激活虚拟环境

| 操作系统             | 激活命令                     |
| -------------------- | ---------------------------- |
| Windows (cmd)        | `.venv\Scripts\activate.bat` |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| macOS / Linux        | `source .venv/bin/activate`  |

激活后，终端提示符前会出现 `(.venv)` 标记，表示当前正在使用虚拟环境：

```bash
$ source .venv/bin/activate
(.venv) $ python --version
Python 3.14.0
```

### `uv` 的自动化虚拟环境管理

使用 `uv` 时，通常不需要手动激活虚拟环境。`uv` 会自动发现并使用项目中的 `.venv`：

```bash
# uv 会自动使用 .venv 中的环境
$ uv add requests
$ uv run python main.py
```

`uv run` 会在隔离的虚拟环境中执行命令，确保依赖不会与全局环境冲突。

### 为什么不一开始就讲虚拟环境？

对于本书前几章的简单练习（每个文件独立、没有外部依赖），直接在系统 Python 中运行是最简单的方式。

但当你的项目开始依赖第三方包时，**总是为每个项目创建独立的虚拟环境**是良好的工程实践。

## 配置国内镜像源

由于网络原因，直接从 PyPI 下载包可能很慢。你可以将 `uv` 的包索引切换为国内镜像，加速下载。

在项目根目录的 `pyproject.toml` 中添加以下内容：

```toml
[tool.uv]
# index-url 指定包下载的镜像源地址
# 这里使用北京外国语大学 (BFSU) 的 PyPI 镜像，下载速度更快
index-url = "https://mirrors.bfsu.edu.cn/pypi/web/simple"

# package = true 表示本项目是一个可安装的包（而非仅脚本）
# 启用此选项后，uv 会支持 uv sync、uv build 等完整命令
package = true
```

> 其他常用的 PyPI 国内镜像源：`https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple`（清华）、`https://pypi.mirrors.ustc.edu.cn/simple/`（中科大）。

通过以上配置，`uv add` 和 `uv sync` 等命令都会通过镜像源下载包，显著提升安装速度。
