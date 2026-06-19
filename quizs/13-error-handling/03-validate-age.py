"""目标：实现 validate_age(age)，如果 age < 0 则抛出 ValueError，
如果 age > 150 也抛出 ValueError，否则返回 None 表示年龄有效。

提示：使用 raise ValueError("描述信息") 来抛出异常。
"""


def validate_age(age: int) -> None:
    """验证年龄是否合法。

    >>> validate_age(25)
    >>> validate_age(0)
    >>> validate_age(150)
    >>> validate_age(-1)
    Traceback (most recent call last):
        ...
    ValueError: 年龄不能为负数
    >>> validate_age(151)
    Traceback (most recent call last):
        ...
    ValueError: 年龄不能超过150
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
