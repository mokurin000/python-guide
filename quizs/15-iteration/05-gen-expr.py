"""目标：使用生成器推导式实现以下函数。

提示：生成器推导式使用圆括号：(expr for item in iterable)。
在函数中直接 return 生成器推导式即可，它会在 sum()、math.prod() 等函数中惰性求值。
"""

import math


def sum_of_squares(n: int) -> int:
    """返回 1² + 2² + ... + n² 的和，使用生成器推导式。

    >>> sum_of_squares(3)
    14
    >>> sum_of_squares(5)
    55
    >>> sum_of_squares(1)
    1
    >>> sum_of_squares(0)
    0
    """
    raise NotImplementedError("代码未实现")


def product_of_odds(n: int) -> int:
    """返回前 n 个奇数的乘积 (1 × 3 × 5 × ...)，使用生成器推导式。

    >>> product_of_odds(3)
    15
    >>> product_of_odds(5)
    945
    >>> product_of_odds(1)
    1
    >>> product_of_odds(0)
    1
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
