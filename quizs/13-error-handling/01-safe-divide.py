"""目标：实现 safe_divide(a, b)，返回 a 除以 b 的结果。
如果 b 为 0，返回 None 而非抛出异常。

提示：使用 try...except 捕获 ZeroDivisionError。
在 except 块中 return None 即可。
"""


def safe_divide(a, b):
    """安全除法，除零时返回 None。

    >>> safe_divide(10, 2)
    5.0
    >>> safe_divide(7, 3)
    2.3333333333333335
    >>> safe_divide(10, 0) is None
    True
    >>> safe_divide(0, 5)
    0.0
    >>> safe_divide(-6, 3)
    -2.0
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
