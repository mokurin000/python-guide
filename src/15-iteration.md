# 迭代器与生成器

在前面的章节中，我们学习了 `list`、`dict`、`set`、`str` 等数据类型，以及如何用 `for` 循环遍历它们。你有没有想过——`for` 循环背后发生了什么？为什么有些对象可以用 `for` 遍历，有些却不行？

本章将揭开这个谜底：**可迭代对象 (Iterable)** 与 **迭代器 (Iterator)** 的概念，以及如何用**生成器 (Generator)** 更简洁地创建迭代器。

## 可迭代对象

> **可迭代对象 (Iterable)** 是可以用 `for` 循环遍历的对象。简单来说，任何可以被 `for` 循环"逐个取出"东西的对象都是可迭代对象。

Python 中常见的内置可迭代对象：

| 类型    | 示例               |
| ------- | ------------------ |
| `list`  | `[1, 2, 3]`        |
| `str`   | `"hello"`          |
| `tuple` | `(1, 2, 3)`        |
| `dict`  | `{"a": 1, "b": 2}` |
| `set`   | `{1, 2, 3}`        |
| `range` | `range(5)`         |

```python
>>> for x in [1, 2, 3]:
...     print(x)
...
1
2
3
>>> for ch in "abc":
...     print(ch)
...
a
b
c
```

### `list()` —— 从可迭代对象创建列表

`list()` 函数可以将任何可迭代对象转换为列表：

```python
>>> list("hello")
['h', 'e', 'l', 'l', 'o']
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list({"a", "b", "c"})
['a', 'c', 'b']  # 集合是无序的，结果顺序可能不同
```

> `list()`、`tuple()`、`set()` 等函数都接受可迭代对象作为参数。这意味着任何可以用 `for` 遍历的东西，都可以用它们来构建新的容器。

### `for` 循环的本质

当我们写 `for x in obj:` 时，Python 实际上做了两件事：

1. 调用 `iter(obj)` 获取一个**迭代器 (Iterator)**
2. 反复调用 `next()` 从迭代器中取值，直到遇到 `StopIteration`

换句话说，`for` 循环是"语法糖"，底层是迭代器协议。

## 迭代器

> **迭代器 (Iterator)** 是一个"逐个产生值"的对象。它知道自己当前的位置，每次调用 `next()` 就返回下一个值。

### `iter()` 与 `next()`

`iter()` 函数从可迭代对象中获取一个迭代器，`next()` 函数从迭代器中获取下一个值：

```python
>>> nums = [1, 2, 3]
>>> it = iter(nums)  # 获取迭代器
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)  # 没有更多元素了
Traceback (most recent call last):
  File "<python-input>", line 1, in <module>
    next(it)
StopIteration
```

这就是 `for` 循环的底层机制！当 `next()` 抛出 `StopIteration` 异常时，`for` 循环知道已经遍历完毕，安静地结束。

> **`StopIteration`** 是迭代器"信号"，表示没有更多元素了。这是异常用于控制流的一个典型例子。

你可以用 `while` 循环手动模拟 `for` 的行为：

```python
>>> it = iter([1, 2, 3])
>>> while True:
...     try:
...         val = next(it)
...         print(val)
...     except StopIteration:
...         break
...
1
2
3
```

### 可迭代对象 vs 迭代器

这两个概念容易混淆，关键区别在于：

- **可迭代对象 (Iterable)**：可以用 `iter()` 从中获取迭代器的对象（如 `list`、`str`）
- **迭代器 (Iterator)**：可以用 `next()` 逐个取值的对象

> 一个常见的误解是"列表就是迭代器"。实际上，列表是**可迭代对象**，但不是迭代器——你不能对列表直接调用 `next()`：

```python
>>> [1, 2, 3][0]  # 列表支持索引
1
>>> next([1, 2, 3])
Traceback (most recent call last):
  File "<python-input>", line 1, in <module>
    next([1, 2, 3])
TypeError: 'list' object is not an iterator
```

需要先用 `iter()` 从列表获取迭代器，才能调用 `next()`。

### 迭代器的"一次性"

**迭代器只能遍历一次**。遍历结束后，它就"耗尽"了：

```python
>>> it = iter([1, 2, 3])
>>> list(it)
[1, 2, 3]
>>> list(it)  # 第二次遍历，结果为空
[]
```

如果需要多次遍历，需要重新创建迭代器（即可迭代对象可以重复使用，迭代器不行）。

## 实现迭代器

> 我们可以自定义一个类，让它实现迭代器协议——即定义 `__iter__()` 和 `__next__()` 方法。

### 迭代器协议

一个迭代器需要实现两个方法：

- **`__iter__()`**：返回迭代器自身（通常在 `for` 循环开头被调用）
- **`__next__()`**：返回下一个值；如果没有更多值，抛出 `StopIteration`

来看一个例子——实现一个从 0 计数到指定上限的迭代器：

```python
>>> class CountUp:
...     def __init__(self, limit):
...         self.current = 0
...         self.limit = limit
...
...     def __iter__(self):
...         return self  # 迭代器返回自身
...
...     def __next__(self):
...         if self.current >= self.limit:
...             raise StopIteration  # 结束信号
...         value = self.current
...         self.current += 1
...         return value
...
>>> counter = CountUp(3)
>>> for n in counter:
...     print(n)
...
0
1
2
```

我们来拆解一下发生了什么：

1. `for n in counter:` 会调用 `iter(counter)`，即 `counter.__iter__()`，返回 `counter` 自身
2. Python 反复调用 `next(counter)`，即 `counter.__next__()`，获取值
3. 当 `current >= limit` 时，`__next__()` 抛出 `StopIteration`，循环结束

> 在迭代器中，`__iter__()` 通常只是返回 `self`。这意味着迭代器同时也是可迭代对象——你可以对它调用 `iter()` 获取自身。

### 可迭代对象 vs 迭代器：分离设计

在上面的例子中，`CountUp` 既是可迭代对象（有 `__iter__`）又是迭代器（有 `__next__`）。但更常见的模式是让**可迭代对象**和**迭代器**分离：

```python
>>> class CountUp:           # 可迭代对象
...     def __init__(self, limit):
...         self.limit = limit
...     def __iter__(self):
...         return CountUpIterator(self.limit)  # 每次返回新迭代器
...
>>> class CountUpIterator:   # 迭代器
...     def __init__(self, limit):
...         self.current = 0
...         self.limit = limit
...     def __iter__(self):
...         return self
...     def __next__(self):
...         if self.current >= self.limit:
...             raise StopIteration
...         value = self.current
...         self.current += 1
...         return value
...
>>> c = CountUp(3)
>>> list(c)
[0, 1, 2]
>>> list(c)  # 可以多次遍历，因为每次 iter() 返回新迭代器
[0, 1, 2]
```

> 这种分离设计的好处是：可迭代对象可以被多次遍历，因为每次调用 `__iter__()` 都会创建一个新的迭代器。

## 生成器

> **生成器 (Generator)** 是用更简洁的语法创建迭代器的方式。你只需要写一个普通函数，但用 `yield` 而不是 `return` 来返回值。

### 生成器函数

当一个函数包含 `yield` 关键字时，它就变成了一个**生成器函数**。调用生成器函数不会直接执行函数体，而是返回一个**生成器对象**（一种特殊的迭代器）：

```python
>>> def count_up(limit):
...     current = 0
...     while current < limit:
...         yield current
...         current += 1
...
>>> gen = count_up(3)  # 不会执行函数体
>>> type(gen)
<class 'generator'>
>>> next(gen)  # 执行到第一个 yield
0
>>> next(gen)  # 从上次 yield 处继续
1
>>> next(gen)  # 继续
2
>>> next(gen)  # 没有更多 yield，抛出 StopIteration
Traceback (most recent call last):
  File "<python-input>", line 1, in <module>
    next(gen)
StopIteration
```

关键区别：

- **`return`**：返回值并退出函数
- **`yield`**：返回值并**暂停**函数执行，下次调用 `next()` 时从暂停处继续

> 生成器函数每次遇到 `yield` 就会"冻结"当前状态（包括所有局部变量的值），等到下次调用 `next()` 时再"解冻"继续执行。

用生成器重写之前的 `CountUp` 迭代器，代码简洁得多：

```python
>>> def count_up(limit):
...     current = 0
...     while current < limit:
...         yield current
...         current += 1
...
>>> for n in count_up(3):
...     print(n)
...
0
1
2
```

用生成器实现的斐波那契数列：

```python
>>> def fibonacci(limit):
...     a, b = 0, 1
...     while a <= limit:
...         yield a
...         a, b = b, a + b
...
>>> list(fibonacci(20))
[0, 1, 1, 2, 3, 5, 8, 13]
```

> 相比于手动实现 `__iter__` 和 `__next__` 的类，生成器函数大幅减少了样板代码。在大多数情况下，如果你需要自定义迭代器，生成器是首选方案。

### 生成器推导式

> **生成器推导式 (Generator Expression)** 类似于列表推导式，但使用圆括号 `()` 而不是方括号 `[]`，并且是惰性求值的。

```python
>>> squares = (x * x for x in range(5))  # 生成器推导式
>>> squares
<generator object <genexpr> at 0x...>
>>> list(squares)
[0, 1, 4, 9, 16]
```

对比列表推导式：

```python
>>> list_comp = [x * x for x in range(5)]  # 立即计算出所有值
>>> gen_expr = (x * x for x in range(5))    # 惰性求值，逐个产生
```

关键区别：

- **列表推导式 `[...]`**：立即计算所有元素，占用内存
- **生成器推导式 `(...)`**：惰性求值，用到时才计算，节省内存

当处理大量数据时，这个区别很重要：

```python
>>> sum(x * x for x in range(1000000))  # 生成器推导式，几乎不占内存
333332833333500000
```

> 注意：如果生成器推导式是函数的唯一参数，可以省略外层括号——就像上面 `sum(...)` 中那样，只需要一层括号。

### 生成器的"一次性"

和所有迭代器一样，生成器也只能遍历一次：

```python
>>> gen = (x * 2 for x in range(5))
>>> list(gen)
[0, 2, 4, 6, 8]
>>> list(gen)  # 已经耗尽
[]
```

如果需要多次使用，可以用 `list()` 将结果保存为列表，或者重新创建生成器。

## 练习

完成 `quizs/15-iteration/*.py`。

你可以直接使用 `▷` 运行对应程序，检查是否通过了测试。

## 附录：生成器的高级方法

生成器对象除了支持 `next()` 之外，还额外提供了三个方法，用于在运行中与生成器交互。

### `.send()` —— 向生成器发送值

`send(value)` 将值发送给生成器，替代当前的 `yield` 表达式的结果，并让生成器继续执行到下一个 `yield`：

```python
>>> def echo():
...     while True:
...         received = yield
...         print(f"收到：{received}")
...
>>> gen = echo()
>>> next(gen)       # 启动生成器，执行到第一个 yield
>>> gen.send("你好")
收到：你好
>>> gen.send(42)
收到：42
```

> 首次与生成器交互必须使用 `next(gen)` 或 `gen.send(None)` 来启动它，因为第一个 `yield` 之前没有 `yield` 表达式可以接收值。

`send()` 也可以配合返回值的 `yield` 实现协程风格的双向通信：

```python
>>> def accumulator():
...     total = 0
...     while True:
...         value = yield total
...         total += value
...
>>> acc = accumulator()
>>> next(acc)   # 启动，返回初始 total
0
>>> acc.send(10)
10
>>> acc.send(5)
15
>>> acc.send(20)
35
```

### `.throw()` —— 向生成器注入异常

`throw(exc_type)` 在生成器暂停的 `yield` 处抛出一个异常。如果生成器内部捕获了该异常，`throw()` 会返回下一个 `yield` 的值；否则异常会传播给调用者：

```python
>>> def safe_divide():
...     try:
...         while True:
...             x, y = yield
...             yield x / y
...     except ZeroDivisionError:
...         yield "除零错误"
...
>>> gen = safe_divide()
>>> next(gen)         # 启动
>>> gen.send((10, 2)) # 正常计算
5.0
>>> gen.throw(ZeroDivisionError)  # 注入异常
'除零错误'
```

### `.close()` —— 关闭生成器

`close()` 在生成器暂停的 `yield` 处注入 `GeneratorExit` 异常，强制生成器退出。如果生成器内部捕获了 `GeneratorExit`，必须重新抛出或直接返回，否则会报错：

```python
>>> def count_down(n):
...     try:
...         while n > 0:
...             yield n
...             n -= 1
...     except GeneratorExit:
...         print("生成器被关闭")
...         raise
...
>>> gen = count_down(3)
>>> next(gen)
3
>>> next(gen)
2
>>> gen.close()
生成器被关闭
```

> 关闭后的生成器不能再使用——任何对它的 `next()` 或 `send()` 调用都会抛出 `StopIteration`。

### 小结

| 方法           | 作用                            |
| -------------- | ------------------------------- |
| `.send(value)` | 向生成器发送值，继续执行        |
| `.throw(exc)`  | 在 `yield` 处注入异常           |
| `.close()`     | 注入 `GeneratorExit` 关闭生成器 |

这三个方法在日常开发中不如 `for` 循环和 `next()` 常用，但它们在实现协程、异步编程、以及复杂生成器控制流时非常重要。
