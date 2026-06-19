"""目标：用递归实现最大公约数函数 gcd(a, b)，使用欧几里得算法。

欧几里得算法（辗转相除法）：
- gcd(a, 0) = a
- gcd(a, b) = gcd(b, a % b)（当 b ≠ 0）

提示：base case 是 b == 0 时返回 a。
递归调用时交换参数位置并对较大数取模。
"""


def gcd(a: int, b: int) -> int:
    """计算 a 和 b 的最大公约数。

    >>> gcd(48, 18)
    6
    >>> gcd(100, 75)
    25
    >>> gcd(17, 13)
    1
    >>> gcd(0, 5)
    5
    >>> gcd(12, 0)
    12
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
