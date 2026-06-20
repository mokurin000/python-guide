"""
目标：理解变量作用域 (scope) ——
块层级内部会直接覆盖函数局部定义变量。
"""

x = 42


def sample() -> int:
    result = x
    if result:
        result = x + 1
    return result


def user_func() -> int:
    """实现一个函数，使其返回值与 sample() 相等。

    >>> user_func() == sample()
    True
    """
    # 修改为正确的数值
    return ...


if __name__ == "__main__":
    # 反射检查：样板函数 sample 不得调用任何函数
    import dis

    calls = [i for i in dis.get_instructions(user_func) if i.opname.startswith("CALL")]
    assert len(calls) == 0, f"返回值函数不得调用任何函数，发现调用：{calls}"

    import doctest

    doctest.testmod(verbose=True)
