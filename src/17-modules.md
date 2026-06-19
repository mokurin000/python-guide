# 模块与导入

在前面的章节中，我们已经多次看到这样的代码：

```python
from functools import reduce
from itertools import pairwise
import math
```

我们在不知不觉中使用了**模块 (module)** 和**导入 (import)**。本章将正式介绍这些概念——它们是你从"写小脚本"迈向"组织大型项目"的关键一步。

## 什么是模块？

**模块 (module)** 就是一个以 `.py` 结尾的 Python 文件。文件中定义的函数、类、变量等，都可以被其他 Python 程序使用。

将代码拆分为多个模块的好处：

- **组织 (Organization)**：把相关功能的代码放在一起
- **复用 (Reusability)**：一个模块可以在多个程序中重复使用
- **命名空间隔离 (Namespace Isolation)**：不同模块可以有同名的函数/变量，互不干扰

## `import` —— 导入模块

### 基本导入

使用 `import` 关键字导入一个完整的模块：

```python
>>> import math
>>> math.sqrt(16)
4.0
>>> math.pi
3.141592653589793
```

导入后，通过 `模块名.名称` 的方式访问模块中的内容。这种方式清晰地表明了名称的来源。

### 选择性导入：`from ... import ...`

如果只需要模块中的某个函数或变量，可以用 `from` 语法：

```python
>>> from math import sqrt, pi
>>> sqrt(25)
5.0
>>> pi
3.141592653589793
```

这样可以直接使用名称，无需加模块前缀。

> **选择哪种方式？** `import math` 更清晰——看到 `math.sqrt` 就知道来自 `math` 模块。`from math import sqrt` 更简洁——适合频繁使用的名称。在大型项目中，清晰的来源往往比少打几个字更重要。

### 起别名：`import ... as ...`

可以为模块或名称指定别名：

```python
>>> import numpy as np
>>> np.array([1, 2, 3])
array([1, 2, 3])

>>> from decimal import Decimal as D
>>> D("3.14")
Decimal('3.14')
```

别名常用于：
- 名称较长的模块（如 `matplotlib.pyplot` 通常简写为 `plt`）
- 避免命名冲突

### 避免 `from ... import *`

```python
>>> from math import *   # 不推荐！
```

这会导入模块中所有不以下划线开头的名称，可能会覆盖当前作用域中已有的变量，导致难以排查的 bug。

> **PEP 8 风格指南**明确建议：在非交互式环境中避免使用通配符导入 (`import *`)。

### 导入风格约定

按照 PEP 8 的建议：

1. `import` 语句放在文件顶部
2. 标准库导入、第三方库导入、本地模块导入之间用空行分隔
3. 每行一个 `import`

```python
import math
import sys
from functools import partial
from pathlib import Path

import requests

from myproject import utils
```

## Python 标准库一览

Python 的一大特色是"自带电池 (Batteries Included)"——安装 Python 时就已经附带了一个庞大的**标准库 (Standard Library)**，涵盖各种常用功能。

下面快速浏览三个最常用的标准库模块：

### `math` —— 数学运算

[官方中文文档](https://docs.python.org/zh-cn/3.14/library/math.html)

```python
>>> import math
>>> math.sqrt(144)          # 平方根
12.0
>>> math.ceil(3.14)         # 向上取整
4
>>> math.floor(3.14)        # 向下取整
3
>>> math.pi                 # 圆周率 π
3.141592653589793
>>> math.inf                # 无穷大
inf
>>> math.isclose(0.1 + 0.2, 0.3)  # 安全比较浮点数
True
```

### `os` —— 操作系统接口

[官方中文文档](https://docs.python.org/zh-cn/3.14/library/os.html)

```python
>>> import os
>>> os.getcwd()                    # 获取当前工作目录
'/home/user/project'
>>> os.listdir(".")                # 列出目录下的文件
['main.py', 'data.txt', 'README.md']
>>> os.path.join("folder", "file.txt")  # 拼接路径（自动使用正确的分隔符）
'folder/file.txt'
>>> os.path.exists("main.py")      # 检查路径是否存在
True
>>> os.name                        # 操作系统名称（'posix'、'nt' 等）
'posix'
```

### `sys` —— Python 运行时环境

[官方中文文档](https://docs.python.org/zh-cn/3.14/library/sys.html)

```python
>>> import sys
>>> sys.argv                       # 命令行参数列表
['myprogram.py', 'arg1', 'arg2']
>>> sys.version                    # Python 版本信息
'3.14.0 (main, ...)'
>>> sys.exit(0)                    # 退出程序（0 表示正常退出）
```

> `os` 和 `sys` 的完整功能远不止这些。遇到操作系统或 Python 运行时的需求时，先看看标准库中是否有现成的工具——很可能有。

### 探索模块：`help()` 和 `dir()`

如果你想知道一个模块提供了什么，可以使用 `dir()`：

```python
>>> import math
>>> dir(math)       # 列出 math 模块中所有名称
['__doc__', '__name__', '__package__', ..., 'acos', 'acosh', 'asin', ...]
```

或者用 `help()` 查看详细文档：

```python
>>> help(math.sqrt)   # 查看 sqrt 函数的文档
```

在交互式环境中，这是探索标准库最快捷的方式。

## `__name__` 与 `if __name__ == "__main__"`

这是每个 Python 学习者迟早会遇到的神秘写法。现在我们来彻底搞懂它。

### 每个模块都有 `__name__`

Python 中的每个模块都有一个内置属性 `__name__`，它的值取决于这个模块是如何被使用的：

- 当模块**直接运行**时，`__name__` 被设置为 `"__main__"`
- 当模块**被导入**时，`__name__` 被设置为**模块的文件名**（不含 `.py`）

创建一个文件 `greet.py`：

```python
# greet.py
def say_hello(name):
    return f"你好，{name}！"

print(f"当前 __name__ 的值是：{__name__}")
```

直接运行它：

```bash
$ python greet.py
当前 __name__ 的值是：__main__
```

在另一个文件中导入它：

```python
>>> import greet
当前 __name__ 的值是：greet
```

### 惯用法：`if __name__ == "__main__"`

利用这个特性，我们可以让一个文件**既可以作为脚本直接运行，又可以作为模块被导入**：

```python
# greet.py
def say_hello(name):
    return f"你好，{name}！"

if __name__ == "__main__":
    # 只有在直接运行时才会执行以下代码
    print(say_hello("世界"))
```

- 当 `python greet.py` 直接运行时，`__name__ == "__main__"` 为真，`say_hello("世界")` 被执行
- 当其他文件 `import greet` 时，`__name__` 为 `"greet"`，条件不成立，`print` 不会执行

> 这就是你一直在使用的 `if __name__ == "__main__":` 的原理！每一个 Quiz 文件的底部都写着它——现在你终于知道它为什么在那里了。

### 典型应用场景

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    # 直接运行时进行快速测试
    print(add(10, 5))       # 15
    print(subtract(10, 5))  # 5
```

被导入时，只提供 `add` 和 `subtract` 函数；直接运行时，还执行测试代码。

## 模块搜索路径

当你执行 `import math` 时，Python 到底去哪里找这个文件？

### `sys.path`

Python 使用一个叫做**模块搜索路径 (module search path)** 的列表来定位模块，这个列表存储在 `sys.path` 中：

```python
>>> import sys
>>> sys.path
['', '/usr/lib/python3.14', '/usr/lib/python3.14/lib-dynload',
 '/usr/local/lib/python3.14/site-packages', ...]
```

### 搜索顺序

Python 按以下顺序在 `sys.path` 中依次查找：

1. **当前脚本所在目录**（或交互式环境的当前工作目录）—— 空字符串 `''` 表示当前目录
2. **`PYTHONPATH` 环境变量**中指定的目录
3. **标准库目录**——Python 自带的模块所在位置
4. **第三方包目录**——`site-packages`，通过 `pip` 或 `uv` 安装的包都在这里

### 为什么要理解搜索路径？

知道 `sys.path` 的存在，你就明白了两件事：

- 为什么 `import math` 能找到标准库——因为标准库目录就在 `sys.path` 中
- 为什么你自己的模块可以被 `import`——因为你当前的工作目录在 `sys.path` 的**最前面**

> 如果你创建了一个与标准库同名的文件（比如 `math.py`），当前目录的优先级更高，Python 会先加载你的文件而不是标准库。这通常会导致意外的错误——**不要用标准库模块名作为你的文件名**。

> **关于 PEP 328（相对导入与绝对导入）**：Python 支持两种导入方式——**绝对导入 (absolute import)**（从 `sys.path` 的根目录开始定位）和**相对导入 (relative import)**（从当前模块所在位置开始，使用 `.` 表示当前目录，`..` 表示上级目录）。相对导入只能在包内部使用，我们将在下一章详细介绍包的概念。

## 小结

| 概念                        | 说明                                      |
| --------------------------- | ----------------------------------------- |
| `import math`               | 导入整个模块，通过 `math.sqrt()` 访问     |
| `from math import sqrt`     | 只导入模块中的特定名称，直接使用 `sqrt()` |
| `import math as m`          | 为模块指定别名                            |
| `from math import *`        | ⚠️ 不推荐，可能污染命名空间                |
| `if __name__ == "__main__"` | 让文件既可被导入又可直接运行              |
| `sys.path`                  | 模块搜索路径列表，Python 按顺序在其中查找 |
| 标准库                      | Python 自带的模块集合，无需额外安装       |

## 练习

完成 `quizs/17-modules/*.py`。

你可以直接使用 `▷` 运行对应程序，检查是否通过了测试。
