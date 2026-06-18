# 内置函数

Python 提供了许多**内置函数**[^1]。调用这些函数时，不需要先从标准库中导入。

[^1]: https://docs.python.org/zh-cn/3.14/library/functions.html

## `int`

```python
>>> int("114_514_1919_810")
1145141919810
>>> int("0o20523761600102", base=8) # 八进制
1145141919810
>>> int("0x10a9fc70042", base=16) # Python 函数支持通过参数名指定参数
1145141919810
```

## `float`

```python
>>> float("-0")
-0.0
>>> float("0.1")
0.1
>>> float("1e-10")
1e-10
>>> float("-inf") # 负无穷大
-inf
>>> 1 / float("+inf") # 正无穷大
0.0
```

## `str`

```python
>>> str(1.0 + 5)
'6.0'
>>> str(2**10)
'1024'
>>> str(1 == 3)
'False'
```

## `bool`

`bool` 的转换规则比较复杂，我们会在学习条件判断时再进一步了解。

## `abs`

`abs()` 函数用于求数字的绝对值。

```python
>>> abs(-1)
1
>>> abs(-1.0)
1.0
```

## `print`

`print()` 函数可以输出数字、布尔值、字符串等类型的数据。

```python
>>> print(1.0)
1.0
>>> print("Hello")
Hello
>>> print(1 == 2)
False
```

## `input`

`input()` 函数可以读取输入。这样一来，我们无需修改程序代码，就可以通过不同的输入重复运行同一个程序。

```python
>>> s = input()
```

输入 `Hello` 后：

```python continue
>>> s
'Hello'
```
