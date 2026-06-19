"""目标：实现 calculate(a, op, b)，支持四则运算。
如果 op 不是 +、-、*、/ 之一，抛出 ValueError。
如果 op 是 / 且 b 为 0，返回 None。

提示：使用多个 except 分支或条件判断来处理不同的错误情况。
可以使用 if-elif 来判断运算符，用 try...except 处理除零错误。
"""


def calculate(a: int | float, op: str, b: int | float) -> int | float | None:
    """简易计算器，支持 +、-、*、/ 四则运算。

    >>> calculate(3, "+", 5)
    8
    >>> calculate(10, "-", 7)
    3
    >>> calculate(4, "*", 3)
    12
    >>> calculate(10, "/", 3)
    3.3333333333333335
    >>> calculate(10, "/", 0) is None
    True
    >>> calculate(5, "%", 2)
    Traceback (most recent call last):
        ...
    ValueError: 不支持的运算符：%
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
