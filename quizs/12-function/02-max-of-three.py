"""目标：定义一个函数 max_of_three(a, b, c)，返回三个数中的最大值。

提示：可以用连续的 if-elif-else 比较，或者直接使用 max() 函数。
max() 函数文档：https://docs.python.org/3/library/functions.html#max
"""


def max_of_three(a: int, b: int, c: int) -> int:
    """返回三个数中的最大值。

    >>> max_of_three(1, 5, 3)
    5
    >>> max_of_three(10, 10, 5)
    10
    >>> max_of_three(-1, -5, 0)
    0
    >>> max_of_three(7, 7, 7)
    7
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
