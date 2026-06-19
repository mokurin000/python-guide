"""目标：实现 fibonacci(limit) 生成器函数，逐个生成不超过 limit 的斐波那契数。

斐波那契数列从 0, 1 开始，后续每个数都是前两个数之和：0, 1, 1, 2, 3, 5, 8, ...

提示：使用 yield 关键字。用两个变量 a, b 分别保存前两个数，
在循环中不断更新 a, b = b, a + b。
"""


def fibonacci(limit: int):
    """生成不超过 limit 的斐波那契数列。

    >>> list(fibonacci(10))
    [0, 1, 1, 2, 3, 5, 8]
    >>> list(fibonacci(1))
    [0, 1, 1]
    >>> list(fibonacci(0))
    [0]
    >>> list(fibonacci(100))
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
