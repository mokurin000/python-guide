# 错误处理

在编写程序时，错误是不可避免的——用户可能会输入无效数据、文件可能不存在、网络可能断开。如果不对这些错误做处理，程序会直接崩溃退出，用户体验很差。

Python 提供了一套**异常处理 (Exception Handling)** 机制，让我们可以优雅地应对错误。

## 什么是异常

> **异常 (Exception)** 是程序运行时发生的错误信号。当 Python 遇到无法继续执行的状况时，它会"抛出 (raise)"一个异常。

如果你还没有学习异常处理，不妨先看看如果程序出现异常会发生什么：

```python
>>> print(1 / 0)
Traceback (most recent call last):
  File "<python-input>", line 1, in <module>
    print(1 / 0)
            ~~^~~
ZeroDivisionError: division by zero
```

程序在这里终止，并显示一个**回溯 (Traceback)**，告诉我们错误类型是 `ZeroDivisionError`，原因是被零除。

### 常见内置异常

| 异常类型            | 含义               | 常见场景             |
| ------------------- | ------------------ | -------------------- |
| `SyntaxError`       | 语法错误           | 漏了冒号、括号不匹配 |
| `NameError`         | 使用了未定义的变量 | 拼写错误、变量未赋值 |
| `TypeError`         | 类型不匹配的操作   | 数字 + 字符串        |
| `ValueError`        | 值不合法           | `int("abc")`         |
| `ZeroDivisionError` | 除零错误           | `1 / 0`              |
| `IndexError`        | 索引超出范围       | 访问不存在的列表元素 |
| `KeyError`          | 字典键不存在       | 访问不存在的字典键   |
| `FileNotFoundError` | 文件不存在         | `open("不存在.txt")` |

> 你在之后的练习中很可能会遇到 `EOFError`，它会在 `input()` 读到文件末尾时抛出（例如在在线评测系统中）。

## try...except

> 使用 `try...except` 可以"捕获"异常，让程序在出错时执行备选逻辑，而不是直接崩溃。

基本语法：

```python
try:
    可能出错的代码
except 异常类型:
    出错时执行的代码
```

来看一个最简单的例子——处理用户输入非数字的情况：

```python
>>> try:
...     num = int(input("请输入一个数字："))
...     print(f"你输入了 {num}")
... except ValueError:
...     print("那不是有效的数字！")
...
请输入一个数字：abc
那不是有效的数字！
```

程序没有崩溃，而是友好地提示用户输入有误。

> 在 `try` 块中，一旦抛出异常，后面的代码将**不再执行**，直接跳到对应的 `except` 块。

### 捕获多个异常类型

一个 `except` 可以同时捕获多种异常类型，用元组 (tuple) 列出：

```python
>>> try:
...     result = 10 / int(input("请输入除数："))
...     print(f"结果是 {result}")
... except (ValueError, ZeroDivisionError):
...     print("输入无效！请输入一个非零数字。")
...
请输入除数：0
输入无效！请输入一个非零数字。
```

### 多个 except 分支

你也可以写多个 `except` 分支，对不同异常做不同处理：

```python
>>> try:
...     result = 10 / int(input("请输入除数："))
...     print(f"结果是 {result}")
... except ValueError:
...     print("请输入有效的数字！")
... except ZeroDivisionError:
...     print("除数不能为零！")
...
请输入除数：0
除数不能为零！
```

> 多个 `except` 分支会按顺序匹配，一旦匹配到某个异常类型，后面的分支就不再检查。

### 捕获所有异常

如果希望捕获所有可能的异常，可以用不带异常类型的 `except`：

```python
try:
    # 某些操作
    ...
except:
    print("出错了！")
```

> 在大多数情况**不推荐**下使用这种写法，因为它会屏蔽掉所有错误信息，包括你意料之外的 bug。
> 
> 更好的做法是指定具体的异常类型。

### 获取异常信息

使用 `as` 关键字可以获取异常对象，从而打印出具体的错误信息：

```python
>>> try:
...     num = int(input("请输入一个数字："))
... except ValueError as e:
...     print(f"错误详情：{e}")
...
请输入一个数字：abc
错误详情：invalid literal for int() with base 10: 'abc'
```

`e` 是一个异常对象，转换成字符串后会显示 Python 内置的错误描述。

## else 与 finally

`try...except` 还可以搭配 `else` 和 `finally` 使用：

```python
try:
    可能出错的代码
except 异常类型:
    出错时执行的代码
else:
    没有出错时执行的代码
finally:
    无论是否出错都会执行的代码
```

### else

`else` 块在 `try` 块没有抛出任何异常时执行：

```python
>>> try:
...     num = int(input("请输入一个数字："))
... except ValueError:
...     print("输入无效！")
... else:
...     print(f"输入有效，数字是 {num}")
...
请输入一个数字：42
输入有效，数字是 42
```

### finally

`finally` 块无论是否发生异常都会执行——即使 `try` 中有 `return` 语句也不例外。它通常用于资源清理，比如关闭文件、释放连接等。

```python
>>> try:
...     f = open("test.txt", "r")
...     content = f.read()
... except FileNotFoundError:
...     print("文件不存在")
... finally:
...     print("清理工作完成")
...
文件不存在
清理工作完成
```

> 本节只是为了让你认识 `finally` 的语法和作用。在之后的章节中，我们将学习 `with` 语句，它可以更简洁地管理资源。

## EOFError

> `EOFError` 会在 `input()` 读取到**文件末尾 (End of File)** 时抛出。

这种情况在交互式终端中不常见，但在**管道重定向**或**在线评测系统**中经常遇到——程序试图读取输入，但已经没有更多数据了。

```python
>>> try:
...     line = input()
... except EOFError:
...     print("没有更多的输入了！")
...
```

当你在命令行用管道传递输入时，如果程序试图读取比可用数据更多的输入行，就会触发 `EOFError`。

处理 `EOFError` 的典型场景：

```python
try:
    while True:
        line = input()
        print(f"读取到：{line}")
except EOFError:
    print("\n输入结束")
```

## raise

> `raise` 关键字用于**手动抛出**异常。

你可以在代码中主动抛出异常，以表示某种不合法的状态：

```python
>>> def set_age(age):
...     if age < 0:
...         raise ValueError("年龄不能为负数")
...     print(f"年龄设置为 {age}")
...
>>> set_age(-5)
Traceback (most recent call last):
  File "<python-input>", line 1, in <module>
    set_age(-5)
    ~~~~~~~~^^^
  File "<python-input>", line 3, in set_age
    raise ValueError("年龄不能为负数")
ValueError: 年龄不能为负数
```

### 重新抛出异常

在 `except` 块中，不带参数的 `raise` 会重新抛出当前捕获的异常：

```python
>>> try:
...     num = int(input("请输入一个数字："))
... except ValueError:
...     print("记录日志：用户输入了无效数字")
...     raise  # 重新抛出，让上层调用者处理
...
```

这个技术在你只想记录错误但让上层代码决定如何处理时很有用。

### 检查异常类型

你也可以使用 `isinstance()` 在捕获通用异常后判断具体类型：

```python
>>> try:
...     result = 10 / int(input("请输入除数："))
... except Exception as e:
...     if isinstance(e, ZeroDivisionError):
...         print("除数不能为零！")
...     elif isinstance(e, ValueError):
...         print("请输入有效的数字！")
...     else:
...         print(f"未知错误：{e}")
...
```

## 练习

完成 `quizs/13-error-handling/*.py`。

你可以直接使用 `▷` 运行对应程序，检查是否通过了测试。
