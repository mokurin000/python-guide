# 循环与遍历

在上一章中，我们学习了列表、字典和集合这三种数据结构。当时我们只能用 `while` 循环来遍历它们，代码写起来有些繁琐。本章将介绍 Python 中更强大、更自然的遍历方式——`for` 循环，以及各种推导式。

## for 循环

> 在其他编程语言中，`for` 循环通常需要用到计数器或索引。但在 Python 中，`for` 循环专门用于**遍历 (iterate)** 任何可迭代对象。

`for` 循环的基本语法是：

```python
for 变量 in 可迭代对象:
    循环体
```

它会把可迭代对象中的每个元素依次赋给变量，然后执行循环体。相比于 `while`，`for` 循环更简洁，也更不容易出错。

```python
>>> fruits = ["苹果", "香蕉", "橘子", "葡萄", "西瓜"]
>>> for fruit in fruits:
...     print(fruit)
...
苹果
香蕉
橘子
葡萄
西瓜
```

### 遍历字符串

字符串也是可迭代的，`for` 循环会逐个取出其中的字符：

```python
>>> for ch in "Python":
...     print(ch)
...
P
y
t
h
o
n
```

## range()

> `range()` 是一个内置函数，用于生成一个整数序列。它常与 `for` 循环配合，实现类似"计数循环"的效果。

### 基本用法

`range()` 有三种调用方式：

```python
>>> for i in range(5):       # 0 到 4
...     print(i, end=" ")
...
0 1 2 3 4

>>> for i in range(2, 7):    # 2 到 6
...     print(i, end=" ")
...
2 3 4 5 6

>>> for i in range(1, 10, 2):  # 1 到 9，步长为 2
...     print(i, end=" ")
...
1 3 5 7 9
```

- `range(stop)`：生成 `0` 到 `stop-1` 的整数
- `range(start, stop)`：生成 `start` 到 `stop-1` 的整数
- `range(start, stop, step)`：生成 `start` 到 `stop-1`，步长为 `step` 的整数

> `range()` 是**左闭右开**的，即包含起始值、不包含结束值。这与列表切片的规则一致。

### 与 while 对比

用 `range()` 实现的计数循环比 `while` 更简短：

```python
# while 方式
i = 0
while i < 5:
    print(i)
    i += 1

# for 方式
for i in range(5):
    print(i)
```

### 活用 range()

```python
# 反向遍历
>>> for i in range(10, 0, -1):
...     print(i, end=" ")
...
10 9 8 7 6 5 4 3 2 1

# 计算 1 到 100 的和
>>> total = 0
>>> for i in range(1, 101):
...     total += i
...
>>> total
5050
```

## 遍历 list

遍历列表是 `for` 循环最常用的场景：

```python
>>> scores = [85, 92, 78, 90, 88]
>>> total = 0
>>> for score in scores:
...     total += score
...
>>> total / len(scores)
86.6
```

### enumerate()：同时获取索引和值

有时我们既需要元素的值，又需要它的索引。这时可以用 `enumerate()`：

```python
>>> fruits = ["苹果", "香蕉", "橘子", "葡萄"]
>>> for i, fruit in enumerate(fruits):
...     print(f"{i}: {fruit}")
...
0: 苹果
1: 香蕉
2: 橘子
3: 葡萄
```

`enumerate()` 默认从 `0` 开始计数。也可以指定起始值：

```python
>>> for i, fruit in enumerate(fruits, start=1):
...     print(f"{i}. {fruit}")
...
1. 苹果
2. 香蕉
3. 橘子
4. 葡萄
```

## 遍历 dict

遍历字典时有几种不同的需求：

```python
>>> student = {"name": "小明", "age": 18, "score": 95.5}

# 遍历键（默认）
>>> for key in student:
...     print(key)
...
name
age
score

# 遍历值
>>> for value in student.values():
...     print(value)
...
小明
18
95.5

# 同时遍历键和值
>>> for key, value in student.items():
...     print(f"{key}: {value}")
...
name: 小明
age: 18
score: 95.5
```

> 注意：遍历字典时，键值对的顺序与插入顺序一致（Python 3.7+ 保证这一点）。

## 遍历 set

集合也是可迭代的，但**无序**，所以遍历时元素的顺序是不确定的：

```python
>>> nums = {5, 2, 8, 1, 9}
>>> for n in nums:
...     print(n, end=" ")
...
1 2 5 8 9  # 实际输出可能不同
```

> 如果你需要有序遍历，可以使用 `sorted()` 对集合排序后再遍历。

## 列表推导式

> **列表推导式 (List Comprehension)** 是一种用简洁语法创建列表的方式。它把 `for` 循环和可选的筛选条件压缩到一行表达式中。

### 基本语法

```python
[表达式 for 变量 in 可迭代对象]
```

```python
# 传统方式
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
# squares = [1, 4, 9, 16, 25]

# 列表推导式
squares = [i ** 2 for i in range(1, 6)]
# [1, 4, 9, 16, 25]
```

可以看到，列表推导式让代码更加简洁、直观。

### 带条件的推导式

```python
[表达式 for 变量 in 可迭代对象 if 条件]
```

```python
# 只保留偶数
>>> nums = [1, 2, 3, 4, 5, 6, 7, 8]
>>> evens = [n for n in nums if n % 2 == 0]
>>> evens
[2, 4, 6, 8]

# 将大于 3 的数字翻倍
>>> doubled = [n * 2 for n in nums if n > 3]
>>> doubled
[8, 10, 12, 16]
```

### 处理字符串

```python
>>> words = ["hello", "world", "python"]
>>> [w.upper() for w in words]
['HELLO', 'WORLD', 'PYTHON']

>>> [len(w) for w in words]
[5, 5, 6]
```

## 字典推导式

字典推导式的语法与列表推导式类似，但使用花括号和键值对表达式：

```python
{键表达式: 值表达式 for 变量 in 可迭代对象}
```

```python
# 将列表中的单词映射为其长度
>>> words = ["苹果", "香蕉", "橘子", "葡萄", "西瓜"]
>>> {w: len(w) for w in words}
{'苹果': 2, '香蕉': 2, '橘子': 2, '葡萄': 2, '西瓜': 2}

# 筛选并转换字典
>>> scores = {"小明": 85, "小红": 92, "小刚": 78, "小丽": 95}
>>> passed = {name: score for name, score in scores.items() if score >= 80}
>>> passed
{'小明': 85, '小红': 92, '小丽': 95}
```

### 反转字典

字典推导式常用来交换字典的键和值：

```python
>>> original = {"a": 1, "b": 2, "c": 3}
>>> reversed_dict = {value: key for key, value in original.items()}
>>> reversed_dict
{1: 'a', 2: 'b', 3: 'c'}
```

> 注意：反转字典时，如果原字典中有重复的值，后面的键会覆盖前面的键。

## 集合推导式

集合推导式也使用花括号，但只写单个表达式（而非键值对）：

```python
{表达式 for 变量 in 可迭代对象}
```

```python
# 计算 1 到 10 中每个数的平方，并去重
>>> squares = {x ** 2 for x in range(1, 10)}
>>> squares
{64, 1, 4, 36, 9, 16, 49, 81, 25}  # 无序

# 筛选字符串中的元音字母（去重）
>>> text = "hello world"
>>> {ch for ch in text if ch in "aeiou"}
{'o', 'e'}  # 无序
```

> 列表推导式用 `[]`、字典推导式用 `{}`（含冒号）、集合推导式也用 `{}`（不含冒号）。注意不要混淆。

## 推导式的性能

推导式不仅写起来简洁，执行效率也通常高于手动 `for` 循环：

```python
# 列表推导式（推荐）
squares = [i ** 2 for i in range(1000)]

# 手动循环（不推荐）
squares = []
for i in range(1000):
    squares.append(i ** 2)
```

在数据量较大时，推导式的性能优势会更加明显。

## 练习

完成 `exercise/11/*.py`。
