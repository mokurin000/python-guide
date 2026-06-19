# 附录：文件读写

在前面的章节中，我们通过 `input()` 和 `print()` 与程序交互——数据随着程序的结束而消失。如果希望数据持久保存——比如保存游戏进度、读取配置文件、记录运行日志——就需要**文件 (File)**。

本附录将系统性地介绍 Python 中的文件读写操作，以及相关的 `pathlib` 和 `json` 模块。

## `open()` —— 打开文件

Python 用内置函数 `open()` 来打开文件并返回一个**文件对象 (File Object)**：

```python
open(file, mode='r', encoding=None)
```

最基本的用法：

```python
>>> f = open("hello.txt", "r", encoding="utf-8")
>>> type(f)
<class '_io.TextIOWrapper'>
>>> f.close()  # 使用完毕后关闭
```

> **文件对象** 是一个代表打开文件的对象，通过它可以读取或写入文件内容。

### 文件模式 (Mode)

`mode` 参数决定了你要对文件做什么操作：

| 模式  | 含义                 | 文件指针位置     | 文件不存在时                               |
| ----- | -------------------- | ---------------- | ------------------------------------------ |
| `'r'` | 读取 (Read)          | 开头             | 抛出 `FileNotFoundError`                   |
| `'w'` | 写入 (Write)         | 开头（清空内容） | 创建新文件                                 |
| `'a'` | 追加 (Append)        | 末尾             | 创建新文件                                 |
| `'x'` | 独占创建 (Exclusive) | 开头             | 创建新文件；已存在则抛出 `FileExistsError` |

```python
>>> f = open("new.txt", "x", encoding="utf-8")  # 创建新文件
>>> f.close()
>>> f = open("new.txt", "x", encoding="utf-8")  # 文件已存在
Traceback (most recent call last):
  ...
FileExistsError: [Errno 17] File exists: 'new.txt'
```

当不指定 `mode` 时，默认使用 `'r'` 模式。

### 编码 (Encoding) —— Windows 用户请注意

`encoding` 参数指定文件的**字符编码 (Character Encoding)**。在 Python 3 中，`open()` 的默认编码取决于操作系统：

- **macOS / Linux**：默认 `utf-8`
- **Windows**：默认使用系统的活动代码页——在中国大陆通常是 `gbk`，而非 `utf-8`

> **在 Windows 上读写文件时，务必显式指定 `encoding="utf-8"`**，否则打开包含中文的文件或写入中文时，可能会出现乱码或编码错误。

```python
# Windows 上的正确做法
f = open("data.txt", "r", encoding="utf-8")
```

这种不一致是导致跨平台代码出现问题的最常见原因之一。

## 读取文件

### `read()` —— 读取全部内容

```python
>>> # 假设 data.txt 的内容是 "Hello\nWorld\n"
>>> f = open("data.txt", "r", encoding="utf-8")
>>> content = f.read()
>>> content
'Hello\nWorld\n'
>>> f.close()
```

`read()` 也可以指定读取的字符数：

```python
>>> f = open("data.txt", "r", encoding="utf-8")
>>> f.read(5)   # 读取前 5 个字符
'Hello'
>>> f.read(3)   # 继续读取接着的 3 个字符
'\nWo'
>>> f.close()
```

### `readline()` —— 逐行读取

```python
>>> f = open("data.txt", "r", encoding="utf-8")
>>> f.readline()
'Hello\n'
>>> f.readline()
'World\n'
>>> f.readline()  # 读取完毕，返回空字符串
''
>>> f.close()
```

### `readlines()` —— 读取所有行

```python
>>> f = open("data.txt", "r", encoding="utf-8")
>>> f.readlines()
['Hello\n', 'World\n']
>>> f.close()
```

### 直接遍历文件对象

文件对象本身是可迭代的，这是最常用、最高效的逐行读取方式：

```python
>>> f = open("data.txt", "r", encoding="utf-8")
>>> for line in f:
...     print(repr(line))
...
'Hello\n'
'World\n'
>>> f.close()
```

这种方式不会一次性将整个文件加载到内存，适合处理大文件。

### 去除换行符

每个读取的行末尾都包含换行符 `\n`，通常需要用 `rstrip()` 去除：

```python
>>> f = open("data.txt", "r", encoding="utf-8")
>>> lines = [line.rstrip('\n') for line in f]
>>> lines
['Hello', 'World']
>>> f.close()
```

> 使用 `line.rstrip('\n')` 而非 `line.strip()`：前者只去掉末尾的换行符，后者会去掉首尾所有的空白字符（包括空格、制表符），可能会改变数据含义。

## 写入文件

### `write()` —— 写入内容

```python
>>> f = open("output.txt", "w", encoding="utf-8")
>>> f.write("Hello, World!\n")
14           # write() 返回写入的字符数
>>> f.write("第二行")
3
>>> f.close()
```

> `'w'` 模式会**清空**文件原有内容再写入。如果文件不存在则创建。

### `writelines()` —— 写入多行

```python
>>> lines = ["第一行\n", "第二行\n", "第三行\n"]
>>> f = open("output.txt", "w", encoding="utf-8")
>>> f.writelines(lines)
>>> f.close()
```

> 注意：`writelines()` 不会自动添加换行符——需要你在字符串中自己包含 `\n`。

### 追加写入

使用 `'a'`（追加）模式在文件末尾添加内容：

```python
>>> f = open("log.txt", "a", encoding="utf-8")
>>> f.write("新日志条目\n")
>>> f.close()
```

## `with` 语句

每次手动调用 `f.close()` 很麻烦，而且如果写入过程中出现异常，文件可能无法正常关闭。

**`with` 语句** 可以自动管理文件的打开和关闭——即使发生异常，文件也会被正确关闭：

```python
>>> with open("data.txt", "r", encoding="utf-8") as f:
...     content = f.read()
...     print(len(content))
...
11
>>> f.closed  # with 块结束后，文件自动关闭
True
```

`with` 语句的通用语法：

```python
with 表达式 as 变量名:
    代码块
```

这种通过 `with` 来管理资源的对象，被称为**上下文管理器 (Context Manager)**。

> **始终使用 `with` 来操作文件。** 它比手动 `open()`/`close()` 更安全、更 Pythonic。你不需要再记住调用 `close()`。

### 同时打开多个文件

```python
>>> with open("a.txt", "r", encoding="utf-8") as f1, \
...      open("b.txt", "r", encoding="utf-8") as f2:
...     a_content = f1.read()
...     b_content = f2.read()
```

## 上下文管理器协议

我们已经看到 `with` 语句可以自动管理文件资源。但 `with` 并不只适用于文件——任何实现了**上下文管理器协议 (Context Manager Protocol)** 的对象都可以使用 `with` 语句。

### `__enter__()` 与 `__exit__()`

上下文管理器协议由两个特殊方法组成：

- **`__enter__(self)`**：在进入 `with` 块时被调用。返回值会被赋值给 `as` 后面的变量。
- **`__exit__(self, exc_type, exc_val, exc_tb)`**：在离开 `with` 块时被调用（无论是否发生异常）。用于执行清理工作，如关闭文件、释放锁等。

`__exit__` 的三个参数：

- `exc_type`：异常类型（如果没有异常则为 `None`）
- `exc_val`：异常实例（如果没有异常则为 `None`）
- `exc_tb`：异常回溯信息（如果没有异常则为 `None`）

如果 `__exit__` 返回 `True`，异常会被"吞没"而不向外传播。

### 自定义上下文管理器

下面是一个计时器上下文管理器，它可以测量代码块的执行时间：

```python
>>> import time
>>> class Timer:
...     def __enter__(self):
...         self.start = time.time()
...         return self
...     def __exit__(self, exc_type, exc_val, exc_tb):
...         self.elapsed = time.time() - self.start
...         print(f"耗时: {self.elapsed:.4f} 秒")
...         return False  # 不处理异常
...
>>> with Timer() as t:
...     sum(range(1000000))
...
耗时: 0.0XXX 秒  # 具体数值取决于运行环境
```

再看一个管理资源的例子——临时文件：

```python
>>> import os
>>> class TempFile:
...     def __init__(self, filename, content=""):
...         self.filename = filename
...         with open(filename, "w", encoding="utf-8") as f:
...             f.write(content)
...     def __enter__(self):
...         return self
...     def __exit__(self, exc_type, exc_val, exc_tb):
...         os.remove(self.filename)  # 离开 with 块时删除文件
...         return False
...
>>> with TempFile("temp.txt", "临时数据") as tf:
...     with open(tf.filename, "r", encoding="utf-8") as f:
...         print(f.read())
...
临时数据
>>> # TempFile 的 __exit__ 已经删除了 temp.txt
>>> os.path.exists("temp.txt")
False
```

### `contextlib.AbstractContextManager`

从 Python 3.6 开始，可以继承 `contextlib.AbstractContextManager` 来显式声明一个类为上下文管理器。这可以像使用 `ABC` 一样提供元类检查：

```python
>>> from contextlib import AbstractContextManager
>>> class ManagedFile(AbstractContextManager):
...     def __init__(self, filename, mode="r", encoding="utf-8"):
...         self.filename = filename
...         self.mode = mode
...         self.encoding = encoding
...     def __enter__(self):
...         self.file = open(self.filename, self.mode, encoding=self.encoding)
...         return self.file
...     def __exit__(self, exc_type, exc_val, exc_tb):
...         self.file.close()
...         return False
...
>>> isinstance(ManagedFile("test.txt"), AbstractContextManager)
True
```

> **建议**：对于简单的上下文管理器，直接定义 `__enter__` 和 `__exit__` 就足够了。`AbstractContextManager` 主要用于需要通过 `isinstance()` 进行类型检查的场景。

### `@contextmanager` 装饰器

除了基于类的实现，`contextlib` 还提供了一个更简洁的方式——`@contextmanager` 装饰器，它基于生成器实现。我们将在下一章学习装饰器后详细说明。

## 文本模式与二进制模式

到目前为止，我们操作的都是**文本文件 (Text File)**——比如 `.txt`、`.py`、`.md`、`.json` 等。但如果要操作图片、音频、视频、压缩包等非文本文件，就需要使用**二进制模式 (Binary Mode)**。

### 二进制模式 `'b'`

在 `mode` 中添加 `'b'` 即可切换到二进制模式：

| 模式   | 含义           |
| ------ | -------------- |
| `'rb'` | 读取二进制文件 |
| `'wb'` | 写入二进制文件 |
| `'ab'` | 追加二进制数据 |

二进制模式下，读取和写入的都是 `bytes` 对象，而非 `str`：

```python
>>> with open("image.jpg", "rb") as f:
...     data = f.read(16)  # 读取前 16 个字节
...     print(type(data))
...     print(data)
...
<class 'bytes'>
b'\xff\xd8\xff\xe0\x00\x10JFIF'  # JPEG 文件头
```

```python
>>> with open("copy.jpg", "wb") as f:
...     f.write(data)  # 写入 bytes 数据
...
16
```

### 文本模式 vs 二进制模式

| 对比项     | 文本模式 (`'r'`/`'w'`)   | 二进制模式 (`'rb'`/`'wb'`) |
| ---------- | ------------------------ | -------------------------- |
| 数据类型   | `str`                    | `bytes`                    |
| 编码处理   | 自动编码/解码            | 不处理编码                 |
| 换行符转换 | 自动转换 (`\n` ↔ `\r\n`) | 不转换                     |
| 适用场景   | 文本文件                 | 图片、音视频、压缩包等     |

> **文本模式下的换行符转换**：在 Windows 上，文本文件中的换行序列是 `\r\n`。文本模式下读取时，Python 会自动将 `\r\n` 转换为 `\n`；写入时则将 `\n` 转换为 `\r\n`。二进制模式下不进行任何转换。正是因此，在文本模式下指定 `encoding` 才有意义——二进制模式不需要编码信息。

## `pathlib` —— 路径操作

在前面我们一直用字符串来表示文件路径，比如 `"data.txt"`、`"folder/file.txt"`。但字符串路径有一些缺点：

- 不同操作系统的路径分隔符不同（Windows 用 `\`，macOS/Linux 用 `/`）
- 拼接路径时容易出错
- 获取文件名、扩展名、父目录等需要调用多个函数

**`pathlib`** 模块提供了面向对象的路径操作，是 Python 3.4+ 中处理路径的推荐方式。

### `Path` 对象

```python
>>> from pathlib import Path
```

#### 创建 Path

```python
>>> p = Path("data/file.txt")
>>> type(p)
<class 'pathlib.Path'>
```

#### 读取文件内容

`Path` 对象提供了直接读写文件的快捷方法：

```python
>>> Path("hello.txt").write_text("Hello, World!", encoding="utf-8")
13
>>> Path("hello.txt").read_text(encoding="utf-8")
'Hello, World!'
```

二进制文件也有对应的 `read_bytes()` 和 `write_bytes()`：

```python
>>> Path("copy.jpg").write_bytes(b'\xff\xd8\xff\xe0')
4
>>> Path("copy.jpg").read_bytes()
b'\xff\xd8\xff\xe0'
```

> `Path.read_text()` 和 `Path.write_text()` 内部使用 `with` 语句管理文件，比手动 `open()`/`close()` 更简洁。

#### 路径属性

```python
>>> p = Path("/home/user/project/data/file.txt")
>>> p.name
'file.txt'
>>> p.stem      # 文件名（不含扩展名）
'file'
>>> p.suffix    # 扩展名
'.txt'
>>> p.parent    # 父目录
PosixPath('/home/user/project/data')
>>> p.parents   # 所有父目录
[PosixPath('/home/user/project/data'), PosixPath('/home/user/project'), ...]
>>> p.root      # 根路径
'/'
>>> p.drive     # 驱动器（Windows 特有）
''
```

在 Windows 上：

```python
>>> p = Path("C:/Users/Alice/data.txt")
>>> p.drive
'C:'
>>> p.root
'\\'
```

#### 路径拼接

`pathlib` 支持使用 `/` 运算符来拼接路径——比字符串拼接更直观、跨平台：

```python
>>> data_dir = Path("data")
>>> file_path = data_dir / "subdir" / "file.txt"
>>> file_path
PosixPath('data/subdir/file.txt')
```

也可以使用 `joinpath()` 方法：

```python
>>> Path("data").joinpath("subdir", "file.txt")
PosixPath('data/subdir/file.txt')
```

> **推荐使用 `/` 运算符**，它更简洁、可读性更强，而且自动处理跨平台路径分隔符差异。

#### 检查路径

```python
>>> p = Path("data.txt")
>>> p.exists()      # 是否存在
True
>>> p.is_file()     # 是否为文件
True
>>> p.is_dir()      # 是否为目录
False
>>> p.is_absolute() # 是否为绝对路径
False
```

#### 列出目录内容

```python
>>> for entry in Path(".").iterdir():
...     print(entry.name)
...
data.txt
output.txt
image.jpg
```

也可以使用 glob 模式匹配：

```python
>>> list(Path(".").glob("*.txt"))
[WindowsPath('data.txt'), WindowsPath('output.txt')]
>>> list(Path(".").rglob("*.py"))  # 递归搜索
[WindowsPath('main.py'), WindowsPath('src/utils.py')]
```

#### 创建和删除目录

```python
>>> Path("new_folder").mkdir()           # 创建目录
>>> Path("new_folder/nested/sub").mkdir(parents=True, exist_ok=True)  # 递归创建
>>> Path("empty_folder").rmdir()         # 删除空目录
```

## `json` —— JSON 数据处理

**JSON (JavaScript Object Notation)** 是一种轻量级的文本数据交换格式，广泛用于 Web API 和配置文件。

Python 的 `json` 模块可以轻松地在 Python 对象和 JSON 字符串之间进行转换。

### JSON 类型对应关系

| JSON      | Python          |
| --------- | --------------- |
| `object`  | `dict`          |
| `array`   | `list`          |
| `string`  | `str`           |
| `number`  | `int` / `float` |
| `boolean` | `bool`          |
| `null`    | `None`          |

### 序列化：`dumps()` / `dump()`

**`json.dumps(obj)`** 将 Python 对象转换为 JSON 字符串：

```python
>>> import json
>>> data = {"name": "Alice", "age": 30, "scores": [88, 92, 85]}
>>> json.dumps(data)
'{"name": "Alice", "age": 30, "scores": [88, 92, 85]}'
```

**`json.dump(obj, file)`** 直接将 Python 对象写入文件：

```python
>>> data = {"name": "Alice", "age": 30}
>>> with open("data.json", "w", encoding="utf-8") as f:
...     json.dump(data, f, ensure_ascii=False, indent=2)
```

#### `indent` —— 美化输出

使用 `indent` 参数让输出更具可读性：

```python
>>> print(json.dumps(data, indent=2))
{
  "name": "Alice",
  "age": 30,
  "scores": [
    88,
    92,
    85
  ]
}
```

常用值：
- `indent=2`：每级缩进 2 个空格（最常用）
- `indent=4`：每级缩进 4 个空格
- `indent=None`：紧凑输出（默认）

#### `ensure_ascii` —— 处理中文

默认情况下，`json.dumps()` 会将所有非 ASCII 字符（如中文）转义为 `\uXXXX` 形式：

```python
>>> json.dumps({"name": "张三"})
'{"name": "\\u5f20\\u4e09"}'
```

指定 `ensure_ascii=False` 可以保留原始字符：

```python
>>> json.dumps({"name": "张三"}, ensure_ascii=False)
'{"name": "张三"}'
```

> **读写包含中文的 JSON 文件时，始终使用 `ensure_ascii=False`**，否则文件中的中文将不可阅读。

### 反序列化：`loads()` / `load()`

**`json.loads(s)`** 将 JSON 字符串转换为 Python 对象：

```python
>>> s = '{"name": "Alice", "age": 30}'
>>> data = json.loads(s)
>>> data
{'name': 'Alice', 'age': 30}
>>> data["name"]
'Alice'
```

**`json.load(file)`** 从文件中读取 JSON 数据：

```python
>>> with open("data.json", "r", encoding="utf-8") as f:
...     data = json.load(f)
...
>>> data
{'name': 'Alice', 'age': 30}
```

### 完整的读写流程

将数据保存到 JSON 文件：

```python
>>> import json
>>> from pathlib import Path
>>> data = [
...     {"name": "Alice", "score": 95},
...     {"name": "Bob", "score": 87},
... ]
>>> Path("scores.json").write_text(
...     json.dumps(data, ensure_ascii=False, indent=2),
...     encoding="utf-8"
... )
```

从 JSON 文件读取数据：

```python
>>> import json
>>> from pathlib import Path
>>> raw = Path("scores.json").read_text(encoding="utf-8")
>>> data = json.loads(raw)
>>> data
[{'name': 'Alice', 'score': 95}, {'name': 'Bob', 'score': 87}]
```

或者直接使用 `json.load()` 配合文件对象：

```python
>>> with open("scores.json", "r", encoding="utf-8") as f:
...     data = json.load(f)
...
>>> data
[{'name': 'Alice', 'score': 95}, {'name': 'Bob', 'score': 87}]
```

> **选择哪种方式？**
> - 如果已经用 `pathlib` 获取了路径，`Path.read_text()` + `json.loads()` 是最简洁的组合
> - 如果需要更精细的控制（如指定文件模式、编码），使用 `open()` + `json.load()`/`json.dump()`

## 练习

完成 `quizs/19-file-io/*.py`，运行方式：

```bash
python quizs/19-file-io/01-read-file.py
```
