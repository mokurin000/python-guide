# 函数与递归

在前面的章节中，我们一直在使用 Python 内置的函数，比如 `print()`、`input()`、`len()`、`range()` 等等。但如果我们需要反复执行某一段逻辑，每次都重写一遍就太繁琐了。这时，我们可以**定义自己的函数 (function)**。

## 定义与调用函数

> 在其他编程语言中，函数也可能被称为**方法 (Method)** 或**子程序 (Subroutine)**。

函数是一段可重复使用的代码块，用 `def` 关键字定义：

```python
def 函数名(参数列表):
    函数体
```

来看一个最简单的例子：

```python
>>> def say_hello():
...     print("你好！")
...
>>> say_hello()  # 调用函数
你好！
```

`say_hello` 是函数名，括号表示调用这个函数。

### 带参数的函数

函数可以接收**参数 (parameter)**，让函数更灵活：

```python
>>> def greet(name):
...     print(f"你好，{name}！")
...
>>> greet("小明")
你好，小明！
>>> greet("小红")
你好，小红！
```

> 在函数定义时，括号中的 `name` 叫**形式参数 (parameter)**；在调用时传入的 `"小明"` 叫**实际参数 (argument)**。

### 函数体与缩进

与 `if`、`while`、`for` 一样，函数体通过**缩进**来界定。函数体内的所有语句都必须缩进一致（通常是 4 个空格）。

```python
def show_info(name, age):
    print(f"姓名：{name}")
    print(f"年龄：{age}")
    # 函数体结束，取消缩进
```

## 返回值

函数可以用 `return` 语句返回一个值。调用函数后，这个值可以被变量接收或直接使用。

```python
>>> def add(a, b):
...     return a + b
...
>>> result = add(3, 5)
>>> result
8
>>> add(10, 20) * 2  # 返回值可以直接参与运算
60
```

如果函数没有 `return` 语句，它会返回 `None`：

```python
>>> def do_nothing():
...     pass
...
>>> print(do_nothing())
None
```

### 返回多个值

Python 的函数可以一次性返回多个值——本质上是通过**元组 (tuple)** 实现的：

> 元组支持类似于列表 (list) 的下标索引、切片语法，切片时结果也是元组。

```python
>>> def min_max(nums) -> tuple:
...     return min(nums), max(nums)
...
>>> result = min_max([3, 1, 7, 2, 9])
>>> result
(1, 9)
>>> type(result)
<class 'tuple'>
```

你也可以用**解包 (unpacking)** 直接把返回值赋给多个变量：

```python
>>> def split_name(full_name: str) -> tuple[str, str]:
...     parts = full_name.split()
...     return parts[0], parts[1]
...
>>> first, last = split_name("张三 李四")
>>> first
'张三'
>>> last
'李四'
```

## 参数默认值

在定义函数时，可以为参数指定**默认值 (default value)**。调用时如果省略该参数，就会使用默认值：

```python
>>> def greet(name, greeting="你好"):
...     return f"{greeting}，{name}！"
...
>>> greet("小明")
'你好，小明！'
>>> greet("小明", "早上好")
'早上好，小明！'
```

> **注意**：带默认值的参数必须放在不带默认值的参数**之后**。`def func(a, b=1)` 是合法的，`def func(a=1, b)` 会报错。

默认值在函数定义时计算一次。对于不可变类型（`int`、`str` 等）这很安全，但**不要**用可变类型（如 `list`、`dict`）作为默认值——这可能导致意料之外的行为。

## 作用域

> **作用域 (Scope)** 决定了变量的可见范围。

在函数内部定义的变量是**局部变量 (local variable)**，只在函数内部可见：

```python
>>> def my_func():
...     x = 10  # 局部变量
...     print(x)
...
>>> my_func()
10
>>> print(x)  # 错误！x 在函数外不可见
Traceback (most recent call last):
  File "<python-input>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
```

在函数外部定义的变量是**全局变量 (global variable)**，可以在函数内部读取，但**不能直接修改**：

```python
>>> count = 0
>>> def increment():
...     print(count)  # 可以读取全局变量
...
>>> increment()
0
```

如果需要在函数内部修改全局变量，需要用 `global` 关键字声明：

```python
>>> count = 0
>>> def increment():
...     global count
...     count += 1
...
>>> increment()
>>> count
1
```

> 通常情况下，应尽量避免在函数内部修改全局变量。更好的做法是把值通过参数传入、通过返回值传出。

### LEGB 规则

Python 查找变量时遵循 **LEGB** 规则（从内到外）：
1. **L**ocal —— 当前函数内部
2. **E**nclosing —— 外层函数（嵌套函数的情况）
3. **G**lobal —— 模块全局
4. **B**uilt-in —— Python 内置作用域

## 递归

> **递归 (Recursion)** 是指函数调用自身的一种编程技巧。

递归的核心思想是：把一个复杂问题分解成与原问题相似、但规模更小的子问题。

### 递归的两个要素

1. **终止条件 (Base Case)**：问题规模足够小，可以直接返回结果
2. **递归步骤 (Recursive Case)**：将问题缩小，调用自身解决子问题

### 阶乘

让我们用递归来实现阶乘 `n!`：

```python
>>> def factorial(n: int):
...     if n <= 1:
...         return 1          # base case
...     return n * factorial(n - 1)  # recursive case
...
>>> factorial(5)
120
```

执行过程如下：

```
factorial(5)
→ 5 * factorial(4)
→ 5 * (4 * factorial(3))
→ 5 * (4 * (3 * factorial(2)))
→ 5 * (4 * (3 * (2 * factorial(1))))
→ 5 * (4 * (3 * (2 * 1)))
→ 5 * (4 * (3 * 2))
→ 5 * (4 * 6)
→ 5 * 24
→ 120
```

### 斐波那契数列

斐波那契数列的定义：`fib(0)=0`，`fib(1)=1`，`fib(n)=fib(n-1)+fib(n-2)`。

```python
>>> def fibonacci(n):
...     if n <= 1: # 递归边界
...         return n
...     return fibonacci(n - 1) + fibonacci(n - 2)  # 递归计算
...
>>> fibonacci(10)
55
```

### 递归与迭代

任何递归都可以用**迭代 (iteration)**（即循环）来改写。递归的代码通常更简洁、更接近数学定义，但可能会消耗更多的内存（调用栈）和时间（重复计算）。

以斐波那契为例，递归版虽然代码优雅，但存在大量重复计算（计算 `fib(5)` 时需要多次计算 `fib(3)`、`fib(2)`）。迭代版更高效：

```python
>>> def fibonacci_iter(n):
...     if n <= 1:
...         return n
...     a, b = 0, 1
...     for _ in range(n):
...         a, b = b, a + b
...     return a
...
>>> fibonacci_iter(10)
55
```

> 当问题天然具有递归结构（如树形遍历、分治算法）时，递归更清晰。当性能或调用深度成为瓶颈时，考虑改用迭代。
>
> 之后我们将会学习如何导入第三方库，通过缓存避免重复计算可以大幅提升递归实现的性能。

## 练习

完成 `quizs/12-function/*.py`。

从本章节开始，你可以直接使用 `▷` 运行对应程序，检查是否通过了测试。

同时，标准答案将不再提供。

## 调用栈

> **调用栈 (Call Stack)** 是程序用来跟踪函数调用的一种数据结构。

每当一个函数被调用，就会在调用栈上"压入"一个新的**栈帧 (stack frame)**，记录函数的参数、局部变量和返回地址。当函数返回时，栈帧被"弹出"。

递归调用会不断向栈中压入新的栈帧：

```
factorial(5)  → 压入
  factorial(4)  → 压入
    factorial(3)  → 压入
      factorial(2)  → 压入
        factorial(1)  → 压入 → 返回 1 → 弹出
      → 返回 2 → 弹出
    → 返回 6 → 弹出
  → 返回 24 → 弹出
→ 返回 120 → 弹出
```

如果递归层数太深（比如试图计算 `factorial(10000)`），会导致**栈溢出 (Stack Overflow)**。

不过，Python 内置了递归层数限制来避免这种情况：

```text
RecursionError: maximum recursion depth exceeded
```

我们可以通过 `sys` 中的一个特殊函数提高最大层数：[^1]

```python
>>> import sys
>>> sys.setrecursionlimit(114514)
>>> sys.getrecursionlimit()      
114514
```

[^1]: https://stackoverflow.com/questions/3323001
