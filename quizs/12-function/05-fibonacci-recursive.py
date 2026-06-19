"""目标：用递归实现斐波那契数列函数 fibonacci(n)，返回第 n 项。

斐波那契数列定义：
- fibonacci(0) = 0
- fibonacci(1) = 1
- fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)（当 n ≥ 2）

提示：递归实现很简单，但效率较低（重复计算多）。
可以先写出 base case (n <= 1)，再写 recursive case。
"""


def fibonacci(n: int) -> int:
    """返回斐波那契数列的第 n 项。

    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(10)
    55
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
