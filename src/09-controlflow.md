# 流程控制

经过前面的学习，我们已经掌握了线性流程程序的开发方式。

然而，如果想要实现更复杂的逻辑，就需要引入更多的流程控制方式。

## 条件判断

> 在开始之前，你可能需要重温一下 [bool 类型](./05-data-types.md#bool)。
>
> 你也可以先完成练习 `08/01-bmi`。

我们先来看一个简单的例子：判断 BMI 所属的类别。

> 我国 18 岁及以上健康成年人的 BMI 正常范围为 18.5kg/m² ≤ BMI < 24.0kg/m²，24.0kg/m² ≤ BMI < 28.0kg/m² 为超重，BMI ≥ 28.0kg/m² 为肥胖。——中国疾病预防控制中心

```python
# 输入体重 (kg)
weight = float(input())
# 输入身高 (cm)
height = int(input()) / 100

# 计算 BMI
bmi = weight / height**2

if bmi < 18.5:
    bmi_type = "过瘦"
elif bmi < 24.0:
    bmi_type = "正常"
elif bmi < 28.0:
    bmi_type = "超重"
else:
    bmi_type = "肥胖"
```

在介绍这段代码的逻辑之前，先观察一下 Python 在逻辑层级发生变化时的写法：

当一个新的代码层级开始时，上一行的末尾会以 `:` 结尾；紧接着，属于新层级的语句需要额外缩进四个空格。

可以看到，上述分支结构由 `if-elif-elif-else`（如果—否则如果—否则如果—否则）组成。其中，只有 `if` 是必须存在的；除 `else` 外，其他分支关键字后都需要编写一个判断表达式。

## 条件分支练习

完成 `exercise/09-a/*.py` 。

## bool 真值转换规则

在条件判断中，我们不仅可以使用逻辑表达式来表示条件的真假。

```python
if 表达式:
    # pass 语句是用于满足 Python 语法要求的空语句
    pass
```

上述代码等价于：

```python
if bool(表达式):
    pass
```

也就是说，条件表达式会先被转换为布尔值。其转换规则如下：

```python
>>> bool(0)  # 整数 0
False
>>> bool(0.0)  # 浮点数 0 或 -0.0
False
>>> bool("")  # 空字符串
False
>>> bool(-1)  # 非 0 整数
True
>>> bool(1e-10)  # 非 0 数值
True
>>> bool("Hello")  # 包含任意内容的字符串（包括空白字符）
True
```

## 条件循环

了解 `if` 语句后，我们已经能够实现简单的逻辑判断。

不过，有些问题仅靠条件判断并不方便解决，因为我们可能需要让某一段代码重复执行多次。

> 在数学中，正整数的**阶乘**是所有小于等于该数的正整数的积，记作 n! ——[维基百科](https://zh.wikipedia.org/zh-cn/阶乘)

例如，如果想仅使用条件判断来计算阶乘，可以写成这样：

```python
n = ... # 输入一个不小于 1 的整数

if n == 1:
    result = 1
elif n == 2:
    result = 1 * 2
elif n == 3:
    result = 1 * 2 * 3
...
```

显然，我们不可能把所有情况都逐一列举出来。

为了解决这类问题，Python 提供了循环语句。

```python
n = ... # 输入一个不小于 1 的整数
current = 1
result = 1

# 只有在 `current <= n` 成立时才开始循环/继续循环
while current <= n:
    # result = result * current
    result *= current
    # current 每次加 1
    current += 1
```

通过 `while` 循环，我们可以从 `1` 开始依次遍历到 `n`，并将这些整数依次相乘，最终得到 `n` 的阶乘。

## 条件循环练习

完成 `exercise/09-b/*.py` 。
