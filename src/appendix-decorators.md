# 附录：装饰器

前面的章节已经覆盖了 Python 的核心知识——从数据类型到控制流程，从函数和类到模块和包，再到文件读写。

本附录将介绍一个在日常开发中极为实用的进阶特性：**函数装饰器 (Decorator)**。

## 函数装饰器

### 函数是一等公民

在 Python 中，函数是**一等公民 (First-class Citizen)**——这意味着函数可以像任何其他对象一样被传递：

```python
>>> def greet(name):
...     return f"你好, {name}!"
...
>>> f = greet      # 赋值给变量
>>> f("Alice")
'你好, Alice!'
>>> list(map(f, ["Bob", "Charlie"]))  # 作为参数传入
['你好, Bob!', '你好, Charlie!']
```

我们已经在[函数式编程](./16-functional.md)一章中见识了高阶函数——接收函数作为参数或返回函数的函数。**装饰器 (Decorator)** 正是建立在这一基础之上。

### 什么是装饰器？

> **装饰器 (Decorator)** 是一个接受函数作为参数并返回一个新函数（或修改后的原函数）的函数。

简单来说，装饰器在**不修改原函数代码**的前提下，给函数"增加额外功能"。

看一个最基础的例子——给函数添加日志输出的装饰器：

```python
>>> def logger(func):
...     def wrapper(*args, **kwargs):
...         print(f"调用: {func.__name__}({args}, {kwargs})")
...         return func(*args, **kwargs)
...     return wrapper
...
>>> def add(a, b):
...     return a + b
...
>>> add = logger(add)  # 手动应用装饰器
>>> add(3, 5)
调用: add((3, 5), {})
8
```

这里发生了什么？

1. `logger` 是一个装饰器函数，它接收 `func` 作为参数
2. `logger` 内部定义了 `wrapper` 函数，它在调用原始 `func` 之前打印了日志
3. `logger` 返回 `wrapper` 函数——一个新的、增强了功能的版本
4. `add = logger(add)` 将原始的 `add` 函数替换为增强后的版本

### `@` 语法糖

上述 `add = logger(add)` 的写法略显繁琐。Python 提供了 `@` 语法糖来简化装饰器的应用：

```python
>>> def logger(func):
...     def wrapper(*args, **kwargs):
...         print(f"调用: {func.__name__}({args}, {kwargs})")
...         return func(*args, **kwargs)
...     return wrapper
...
>>> @logger
... def add(a, b):
...     return a + b
...
>>> add(3, 5)
调用: add((3, 5), {})
8
```

`@logger` 放在函数定义之前，完全等价于 `add = logger(add)`。

> **`@` 语法糖**只是让代码更简洁、更优雅。理解"装饰器 = 接受函数并返回函数的高阶函数"这一本质，比记住语法更重要。

### 实际应用：计时装饰器

统计函数执行时间是一个常见的需求：

```python
>>> import time
>>> def timer(func):
...     def wrapper(*args, **kwargs):
...         start = time.time()
...         result = func(*args, **kwargs)
...         elapsed = time.time() - start
...         print(f"{func.__name__} 耗时: {elapsed:.4f} 秒")
...         return result
...     return wrapper
...
>>> @timer
... def slow_sum(n):
...     return sum(range(n))
...
>>> slow_sum(10_000_000)
slow_sum 耗时: 0.XXXX 秒  # 取决于运行环境
49999995000000
```

### 实际应用：缓存/记忆化

对于计算密集型的纯函数，可以缓存结果避免重复计算：

```python
>>> def memoize(func):
...     cache = {}
...     def wrapper(n):
...         if n not in cache:
...             cache[n] = func(n)
...         return cache[n]
...     return wrapper
...
>>> @memoize
... def fib(n):
...     if n < 2:
...         return n
...     return fib(n - 1) + fib(n - 2)
...
>>> fib(100)
354224848179261915075
```

> 实际开发中，请使用 `functools.lru_cache` 或 `functools.cache` 而非手动实现缓存。此处仅为演示装饰器的原理。

### 装饰器叠加

多个装饰器可以叠加使用，按照**从下到上**的顺序应用：

```python
>>> def bold(func):
...     def wrapper():
...         return f"<b>{func()}</b>"
...     return wrapper
...
>>> def italic(func):
...     def wrapper():
...         return f"<i>{func()}</i>"
...     return wrapper
...
>>> @bold
... @italic
... def greet():
...     return "Hello"
...
>>> greet()
'<b><i>Hello</i></b>'
```

`@bold` 和 `@italic` 叠加等价于 `greet = bold(italic(greet))`——先应用 `italic`，再应用 `bold`。从被装饰函数的角度看，离它最近的装饰器最先执行。

### `functools.wraps` —— 保留元数据

装饰器有一个副作用——它会用 `wrapper` 函数替换原始函数，导致原始函数的元数据丢失：

```python
>>> def logger(func):
...     def wrapper(*args, **kwargs):
...         print(f"调用: {func.__name__}")
...         return func(*args, **kwargs)
...     return wrapper
...
>>> @logger
... def add(a, b):
...     """返回两数之和。"""
...     return a + b
...
>>> add.__name__
'wrapper'  # 本应是 'add'
>>> add.__doc__
None       # 本应是 '返回两数之和。'
```

`functools.wraps` 是一个辅助装饰器，可以将原始函数的元数据复制到 `wrapper` 函数上：

```python
>>> from functools import wraps
>>> def logger(func):
...     @wraps(func)
...     def wrapper(*args, **kwargs):
...         print(f"调用: {func.__name__}")
...         return func(*args, **kwargs)
...     return wrapper
...
>>> @logger
... def add(a, b):
...     """返回两数之和。"""
...     return a + b
...
>>> add.__name__
'add'
>>> add.__doc__
'返回两数之和。'
```

`@wraps(func)` 还会复制 `__module__`、`__qualname__`、`__dict__`、`__annotations__` 等属性，并将 `__wrapped__` 属性设置为原始函数，以便其他工具（如 `inspect` 模块）能够正确解包。

> **定义装饰器时，始终使用 `@functools.wraps`**。这是一个好习惯，可以避免调试时被"丢失的函数名"迷惑。

### 内置装饰器

Python 自带了几个非常有用的装饰器，你可能已经在使用了：

#### `@property`

将方法变成属性访问：

```python
>>> class Circle:
...     def __init__(self, radius):
...         self._radius = radius
...     @property
...     def area(self):
...         return 3.14159 * self._radius ** 2
...
>>> c = Circle(5)
>>> c.area        # 像访问属性一样调用方法，而非 c.area()
78.53975
```

#### `@staticmethod` 和 `@classmethod`

```python
>>> class MathUtils:
...     @staticmethod
...     def add(a, b):
...         return a + b
...     @classmethod
...     def from_string(cls, s):
...         return cls()
...
>>> MathUtils.add(3, 5)
8
```

#### `@functools.lru_cache` / `@functools.cache`

自动记忆函数返回值：

```python
>>> from functools import lru_cache
>>> @lru_cache(maxsize=128)
... def fib(n):
...     if n < 2:
...         return n
...     return fib(n - 1) + fib(n - 2)
...
>>> fib(50)
12586269025
```

## 练习

完成 `quizs/20-advanced/*.py`，运行方式：

```bash
python quizs/20-advanced/01-logging-decorator.py
```
