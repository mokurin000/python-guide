# 包与项目

上一章我们学习了如何导入和使用模块。当模块越来越多时，自然需要一种方式将它们组织起来——这就是**包 (Package)**。

本章还将介绍现代 Python 项目工具 [uv]，并通过一个完整的 `pygrep` 示例，展示如何从零开始创建和组织一个真正的 Python 项目。

[uv]: https://docs.astral.sh/uv/getting-started/installation/

## 什么是包

**包 (Package)** 是一个包含多个模块的目录。它让模块有了层次结构，就像文件系统中的目录和子目录。

### 创建一个包

包在文件系统上就是一个目录，里面可以包含多个 `.py` 文件（即模块）。为了让 Python 将该目录视为包，目录中通常包含一个 `__init__.py` 文件。

例如，本书提供的 `messager` 包（位于 `quizs/18-packages/messager/`）：

```
messager/
├── pyproject.toml
├── README.md
└── src/
    └── messager/
        ├── __init__.py
        ├── email.py
        └── sms.py
```

```python
# src/messager/email.py
def send(to, subject, body):
    return f"发送邮件到 {to}：{subject}"
```

```python
# src/messager/sms.py
def send(phone, message):
    return f"发送短信到 {phone}：{message}"
```

### 导入包中的模块

```python
>>> import messager.email
>>> messager.email.send("alice@example.com", "你好", "Hello!")
'发送邮件到 alice@example.com：你好'

>>> from messager.sms import send
>>> send("13800138000", "包的概念很简单")
'发送短信到 13800138000：包的概念很简单'
```

### `__init__.py` 的作用

`__init__.py` 在包被导入时自动执行，常用于：

- 初始化包级别的数据
- 控制 `from package import *` 的导出内容（通过 `__all__`）
- 将子模块中的名称"提升"到包级别

```python
# src/messager/__init__.py
from .email import send as send_email
from .sms import send as send_sms

__all__ = ["send_email", "send_sms"]
```

有了 `__init__.py` 后，可以这样导入：

```python
>>> from messager import send_email
>>> send_email("alice@example.com", "你好", "Hello!")
'发送邮件到 alice@example.com：你好'
```

> 在 Python 3.3+ 中，即使没有 `__init__.py` 文件，目录也可以被视为包，这称为**隐式命名空间包 (Implicit Namespace Package)**。但对于大多数项目，显式添加 `__init__.py` 仍然是好习惯。

### 子模块

包可以嵌套——包中的子目录就是子模块 (sub-module)：

```
messager/
└── src/
    └── messager/
        ├── __init__.py
        ├── email.py
        ├── sms.py
        └── providers/
            ├── __init__.py
            ├── sendgrid.py
            └── twilio.py
```

```python
>>> from messager.providers.sendgrid import send_via_sendgrid
```

## 使用 `uv` 创建项目

了解了模块和包的概念后，我们来看看如何用现代工具 `uv` 创建和组织一个完整的 Python 项目。

### `uv` 简介

`uv` 是一个用 Rust 编写的极速 Python 包管理器和项目管理工具，由 Astral 团队开发。它可以作为 `pip`、`pip-tools`、`pipenv`、`poetry` 等工具的替代方案。

> 如果你还没有安装 `uv`，可以访问 [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/) 了解安装方法。

### `uv init` —— 创建新项目

```bash
$ uv init pygrep
```

执行后，`uv` 会生成以下项目结构：

```
pygrep/
├── pyproject.toml
├── README.md
└── src/
    └── pygrep/
        ├── __init__.py
        └── pyproject.toml  # 符号链接
```

### `src/` 布局

`uv` 默认使用 **`src` 布局 (`src` layout)**，即项目的源代码放在 `src/` 子目录下：

```
pygrep/
├── pyproject.toml       # 项目配置
├── README.md
└── src/
    └── pygrep/           # 实际的包目录
        ├── __init__.py
        └── ...
```

**为什么推荐 `src/` 布局？**

- **清晰的分离**：源代码与配置文件、文档、测试等处于同一层级但相互独立
- **避免导入混乱**：没有 `src/` 时，项目根目录就在 `sys.path` 中，可能导致错误的导入行为
- **符合社区惯例**：越来越多的现代 Python 项目采用此布局

### `pyproject.toml` 文件

`uv init` 生成的 `pyproject.toml` 内容大致如下：

```toml
[project]
name = "pygrep"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []
```

`pyproject.toml` 是 Python 项目的标准配置文件，定义了项目名称、版本、依赖等信息。我们将在附录中详细介绍如何配置它。

## 最小示例：`pygrep`

下面通过一个完整的项目示例，看看模块、包、`__name__` 和 `uv` 是如何协同工作的。

`pygrep` 是一个极简的文本搜索工具，功能类似于 `grep`。它检查文本中是否包含某个字符串，支持读取文件或标准输入。

### 项目结构

```
pygrep/
├── pyproject.toml
└── src/
    └── pygrep/
        ├── __init__.py
        ├── __main__.py
        └── core.py
```

### `core.py` —— 核心逻辑

这个模块负责文本匹配，是纯逻辑层，没有输入输出操作：

```python
# src/pygrep/core.py
def contains(pattern: str, text: str) -> bool:
    """检查 text 中是否包含 pattern。"""
    return pattern in text


def filter_lines(pattern: str, lines: list[str]) -> list[str]:
    """返回包含 pattern 的所有行。"""
    return [line for line in lines if contains(pattern, line)]
```

### `__main__.py` —— 程序入口

`__main__.py` 是 Python 包的入口点。当通过 `python -m pygrep` 运行包时，Python 会自动执行此文件。它使用 `if __name__ == "__main__"` 惯用法：

```python
# src/pygrep/__main__.py
import sys
from .core import filter_lines


def main():
    if len(sys.argv) < 2:
        print("用法: pygrep <pattern> [文件...]")
        print("       <命令> | pygrep <pattern>")
        sys.exit(1)

    pattern = sys.argv[1]

    if len(sys.argv) >= 3:
        # 从文件中读取
        for filepath in sys.argv[2:]:
            try:
                with open(filepath, encoding="utf-8") as f:
                    lines = f.readlines()
            except FileNotFoundError:
                print(f"文件未找到: {filepath}", file=sys.stderr)
                continue

            matched = filter_lines(pattern, lines)
            for line in matched:
                print(line, end="")
    else:
        # 从标准输入读取
        lines = sys.stdin.readlines()
        matched = filter_lines(pattern, lines)
        for line in matched:
            print(line, end="")


if __name__ == "__main__":
    main()
```

### `__init__.py` —— 导出公共接口

```python
# src/pygrep/__init__.py
from .core import contains, filter_lines

__all__ = ["contains", "filter_lines"]
```

### 运行 `pygrep`

使用 `uv run` 可以在不事先安装包的情况下直接运行：

```bash
$ cd pygrep

# 搜索文件中包含 "import" 的行
$ uv run python -m pygrep import src/pygrep/core.py
from .core import filter_lines

# 通过管道搜索（查看当前目录中哪些文件包含 "py"）
$ ls | uv run python -m pygrep py
pygrep
```

> `python -m <包名>` 告诉 Python"以模块/包的方式运行"。Python 会执行该包的 `__main__.py` 文件。

### 代码回顾

这个例子综合运用了我们学过的多个概念：

- **模块组织**：将核心逻辑 (`core.py`) 与入口点 (`__main__.py`) 分离
- **包结构**：`pygrep/` 目录是一个包，包含 `__init__.py`
- **`if __name__ == "__main__"`**：`__main__.py` 中的惯用法
- **标准库**：`sys.argv` 读取命令行参数，`sys.stdin` 读取标准输入
- **`uv` 管理项目**：`uv init` 创建结构，`uv run` 执行

## 小结

| 概念                | 说明                                     |
| ------------------- | ---------------------------------------- |
| 包 (Package)        | 包含多个模块的目录，通常含 `__init__.py` |
| `__init__.py`       | 包初始化文件，在包被导入时执行           |
| 子模块 (Sub-module) | 包中的子目录                             |
| `uv init`           | 创建现代 Python 项目结构                 |
| `src/` 布局         | 源码放在 `src/` 下，分离关注点           |
| `python -m <包名>`  | 以模块方式运行包，执行 `__main__.py`     |

## 练习

完成 `quizs/18-packages/messager/quiz/01-send-message.py`。

这个练习需要从真实的 `messager` 包中导入模块并调用函数。请先进入该包目录，然后用 `uv run` 在虚拟环境中运行：

```bash
$ cd quizs/18-packages/messager
$ uv run python quiz/01-send-message.py
```

> 在 VS Code 中，可以使用 <kbd>Ctrl</kbd> + <kbd>`</kbd>（反引号）快速打开终端，然后输入上述命令。

第一次运行时，`uv` 会自动创建虚拟环境并安装 `messager` 包。
