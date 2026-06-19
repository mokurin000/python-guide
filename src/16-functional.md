# 函数式编程

在上一章中，我们学习了迭代器与生成器——Python 中处理序列数据的强大工具。从生成器推导式到 `yield`，我们看到了如何"按需"产生数据。

本章将更进一步，探索 Python 中的**函数式编程 (Functional Programming)** 风格。函数式编程的核心思想是：**把函数当作值来传递**——函数可以像整数、字符串一样被赋值给变量，作为参数传入另一个函数，或者作为返回值。

Python 虽然不是纯函数式语言，但它提供了一系列实用的函数式编程工具，让我们能写出更简洁、更具表达力的代码。

## 匿名函数 `lambda`

> **`lambda`** 是 Python 中创建小型匿名函数的关键字。所谓"匿名"，即不需要像 `def` 那样给函数起名字。

`lambda` 的语法非常简单：

```python
lambda 参数列表: 表达式
```

它等价于：

```python
def 函数名(参数列表):
    return 表达式
```

来看一个对比。定义一个返回两数之和的函数：

```python
>>> def add(a, b):
...     return a + b
...
>>> add(3, 5)
8
```

用 `lambda` 改写：

```python
>>> lambda a, b: a + b
<function <lambda> at 0x...>
```

如果不赋值，`lambda` 表达式只是创建了一个函数对象，但无法复用。通常我们会将它赋值给变量，或直接作为参数传入其他函数：

```python
>>> add = lambda a, b: a + b
>>> add(3, 5)
8
```

> 虽然可以赋值给变量，但 PEP 8 风格指南建议：如果需要给函数起名字，应该用 `def` 而非 `lambda`。`lambda` 的优势在于"用完即走"的临时场景。

### 常见用法：排序 key

`sorted()` 和 `list.sort()` 接受一个 `key` 参数，用于指定排序规则。`lambda` 非常适合在此处使用：

```python
>>> students = [("Alice", 22), ("Bob", 19), ("Charlie", 21)]
>>> sorted(students, key=lambda s: s[1])  # 按年龄排序
[('Bob', 19), ('Charlie', 21), ('Alice', 22)]
```

```python
>>> words = ["banana", "apple", "cherry", "date"]
>>> sorted(words, key=lambda w: len(w))  # 按长度排序
['date', 'apple', 'banana', 'cherry']
```

### 常见用法：条件表达式

`lambda` 体内只能写一个表达式（不能写语句），但表达式可以包含条件运算符：

```python
>>> max_val = lambda a, b: a if a > b else b
>>> max_val(10, 20)
20
```

## `map()` —— 映射

> **`map(func, iterable)`** 将函数 `func` 应用到 `iterable` 的每一个元素上，返回一个迭代器 (iterator)。

这是函数式编程中最基础的"映射"操作——把一种形式的序列映射为另一种形式。

```python
>>> numbers = [1, 2, 3, 4, 5]
>>> squares = map(lambda x: x ** 2, numbers)
>>> list(squares)
[1, 4, 9, 16, 25]
```

`map` 返回的是一个惰性求值的迭代器，需要用 `list()` 将其转换为列表，或通过 `for` 循环遍历。

```python
>>> names = ["alice", "bob", "charlie"]
>>> for name in map(str.upper, names):
...     print(name)
...
ALICE
BOB
CHARLIE
```

也可以传入多个可迭代对象，函数应接受相应数量的参数：

```python
>>> list(map(lambda a, b: a + b, [1, 2, 3], [10, 20, 30]))
[11, 22, 33]
```

当多个可迭代对象长度不一致时，`map` 会在最短的那个耗尽时停止。

> **对比列表推导式：** `map` 能做的，列表推导式通常也能做。`[x ** 2 for x in numbers]` 等价于 `list(map(lambda x: x ** 2, numbers))`。选择哪种风格主要是代码可读性的考量。

## `filter()` —— 过滤

> **`filter(predicate, iterable)`** 用 `predicate`（谓词，即返回 `bool` 的函数）测试每个元素，只保留使谓词返回 `True` 的元素，返回一个迭代器。

```python
>>> numbers = [1, 2, 3, 4, 5, 6]
>>> evens = filter(lambda x: x % 2 == 0, numbers)
>>> list(evens)
[2, 4, 6]
```

```python
>>> words = ["hello", "", "world", "", "!"]
>>> list(filter(lambda w: len(w) > 0, words))  # 过滤空字符串
['hello', 'world', '!']
```

如果 `predicate` 为 `None`，则会过滤掉所有"假值"（`False`、`None`、`0`、`""` 等）：

```python
>>> values = [0, 1, "", "hello", None, True, False]
>>> list(filter(None, values))
[1, 'hello', True]
```

> **对比列表推导式：** `[x for x in numbers if x % 2 == 0]` 等价于 `list(filter(lambda x: x % 2 == 0, numbers))`。

### 组合 `map` 和 `filter`

`map` 和 `filter` 可以串联使用，构成数据处理管道：

```python
>>> numbers = [1, 2, 3, 4, 5, 6]
>>> # 先过滤出偶数，再求平方
>>> result = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
>>> list(result)
[4, 16, 36]
```

## `functools.reduce()` —— 累积

> **`reduce(func, sequence[, initial])`** 将函数 `func` 累积地应用到序列的元素上，将序列归约为一个单一的值。

`reduce` 位于 `functools` 模块中，使用前需要先导入：

```python
from functools import reduce
```

### 工作原理

`reduce` 的执行过程如下：

1. 如果提供了 `initial` 值，从 `initial` 开始，否则从序列的第一个元素开始
2. 将当前结果与序列的下一个元素传递给 `func`，得到新的结果
3. 重复步骤 2，直到序列耗尽
4. 返回最终结果

例如，`reduce(lambda a, b: a + b, [1, 2, 3, 4])` 的执行过程：

```
初始: a = 1, b = 2 → 3
第2步: a = 3, b = 3 → 6
第3步: a = 6, b = 4 → 10
结果: 10
```

### 基本示例

```python
>>> from functools import reduce
>>> reduce(lambda a, b: a + b, [1, 2, 3, 4])   # 求和
10
>>> reduce(lambda a, b: a * b, [1, 2, 3, 4])   # 求积
24
```

指定 `initial` 值（相当于在序列最前面插入该值）：

```python
>>> reduce(lambda a, b: a + b, [1, 2, 3, 4], 100)  # 100 + 1 + 2 + 3 + 4
110
```

### 进阶示例：杨辉三角

杨辉三角（Pascal's Triangle）每一行的数字由上一行相邻两数之和得到：

```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

生成杨辉三角的过程天然适合 `reduce`——每次迭代根据当前行计算出下一行，并将新行追加到结果列表中。

先实现生成单行的函数：

```python
>>> from itertools import pairwise
>>> def next_row(prev: list[int]) -> list[int]:
...     """根据上一行生成下一行"""
...     return [1] + list(map(sum, pairwise(prev))) + [1]
...
>>> next_row([1, 2, 1])
[1, 3, 3, 1]
```

然后用 `reduce` 将每行逐步累积起来：

```python
>>> from functools import reduce
>>> def yanghui_triangle(n: int) -> list[list[int]]:
...     """生成杨辉三角的前 n 行"""
...     if n <= 0:
...         return []
...     return reduce(
...         lambda acc, _: acc + [next_row(acc[-1])],  # 取最后一行，计算出下一行
...         range(n - 1),  # 剩余行数
...         [[1]]  # 杨辉三角的第一行
...     )
...
>>> yanghui_triangle(5)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

在这个例子中：

- **累加器 `acc`**：类型是 `list[list[int]]`，保存已生成的所有行
- **`acc + [next_row(...)]`**：追加新行

## `functools.partial()` —— 偏函数

> **`partial(func, *args, **kwargs)`** 固定函数的部分参数，返回一个新函数，新函数调用时只需要传入剩余的参数。

有时我们有一个通用的函数，但在某个场景下需要反复使用相同的参数。`partial` 可以将这些参数"冻结"，创建一个更特化的版本。

```python
>>> from functools import partial
>>> def power(base, exp):
...     return base ** exp
...
>>> square = partial(power, exp=2)
>>> cube = partial(power, exp=3)
>>> square(5)
25
>>> cube(5)
125
```

### 按位置固定参数

```python
>>> def greet(greeting, name):
...     return f"{greeting}, {name}!"
...
>>> say_hello = partial(greet, "Hello")
>>> say_hello("Alice")
'Hello, Alice!'
>>> say_hello("Bob")
'Hello, Bob!'
```

### 实际应用场景

`partial` 在回调函数、事件处理、以及需要适配函数接口时非常有用。例如，将一个多参数函数转换成只需要一个参数的函数（以便传入只需单参数的 `map` 或 `filter`）：

```python
>>> def divide(a, b):
...     return a / b
...
>>> # 固定除数为 2
>>> half = partial(divide, b=2)
>>> list(map(half, [10, 20, 30, 40]))
[5.0, 10.0, 15.0, 20.0]
```

另一个常见场景是设置默认参数不同的"副本"：

```python
>>> import math
>>> # 创建一个以 10 为底的对数函数
>>> log10 = partial(math.log, base=10)
>>> log10(100)
2.0
>>> log10(1000)
3.0
```

> `partial` 并不执行函数，它只是创建一个包装后的新函数。实际的参数绑定在调用时才发生。

## 小结

| 工具                     | 作用                     | 来自        |
| ------------------------ | ------------------------ | ----------- |
| `lambda`                 | 创建匿名函数             | 内置        |
| `map(func, iterable)`    | 映射：对每个元素应用函数 | 内置        |
| `filter(pred, iterable)` | 过滤：保留满足条件的元素 | 内置        |
| `reduce(func, seq)`      | 累积：将序列归约为单一值 | `functools` |
| `partial(func, *args)`   | 偏函数：固定部分参数     | `functools` |

这些函数式编程工具让 Python 的代码更加灵活、简洁。在实际项目中，它们常常与列表推导式、生成器推导式等 Python 特性配合使用，形成清晰的数据处理管道。

## 练习

完成 `quizs/16-functional/*.py`。

你可以直接使用 `▷` 运行对应程序，检查是否通过了测试。
