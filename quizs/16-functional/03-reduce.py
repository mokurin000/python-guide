"""目标：使用 functools.reduce() 进行累积运算。

实现以下函数，使用 `reduce(func, sequence[, initial])` 来归约序列。

提示：
- 从 functools 模块导入 reduce
- reduce 将函数累积应用到序列元素上，将序列归约为一个值
- `reduce(lambda a, b: ..., seq)` 从 seq[0] 开始
- `reduce(lambda a, b: ..., seq, initial)` 从 initial 开始
"""

from functools import reduce


def product(numbers: list[int]) -> int:
    """计算列表中所有数字的乘积。

    >>> product([1, 2, 3, 4])
    24
    >>> product([5])
    5
    >>> product([])
    1
    """
    raise NotImplementedError("代码未实现")


def max_with_reduce(numbers: list[int]) -> int | None:
    """使用 reduce 找出列表中的最大值。空列表返回 None。

    >>> max_with_reduce([3, 7, 2, 9, 5])
    9
    >>> max_with_reduce([-5, -2, -10])
    -2
    >>> max_with_reduce([]) is None
    True
    """
    raise NotImplementedError("代码未实现")


def factorial_reduce(n: int) -> int:
    """使用 reduce 计算 n 的阶乘。0! = 1。

    >>> factorial_reduce(5)
    120
    >>> factorial_reduce(0)
    1
    >>> factorial_reduce(1)
    1
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
