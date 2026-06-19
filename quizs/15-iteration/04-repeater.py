"""目标：实现 repeater(item, times) 生成器函数，将 item 重复生成 times 次。
如果 times 为 0 或负数，则不产生任何值。

提示：使用 for 循环配合 range(times)，在循环体内用 yield 返回 item。
"""


def repeater(item, times: int):
    """重复生成 item 共 times 次。

    >>> list(repeater("A", 3))
    ['A', 'A', 'A']
    >>> list(repeater(42, 5))
    [42, 42, 42, 42, 42]
    >>> list(repeater("X", 0))
    []
    >>> list(repeater("hello", 1))
    ['hello']
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
