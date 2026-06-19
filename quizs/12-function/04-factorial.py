"""目标：用递归实现阶乘函数 factorial(n)，返回 n!。

阶乘定义：n! = n × (n-1) × (n-2) × ... × 1，且 0! = 1。

提示：递归需要 base case（终止条件）和 recursive case（递归调用自身）。
n! 的递归形式：n! = n × (n-1)!，当 n <= 1 时返回 1。
"""


def factorial(n: int) -> int:
    """计算 n 的阶乘。

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(10)
    3628800
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
