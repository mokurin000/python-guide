"""目标：实现 StepRange 类，使其成为一个迭代器，从 start 开始以 step 步长递增，
直到（但不包括）end。与内置 range() 类似。

例如 StepRange(0, 10, 3) 依次产生 0, 3, 6, 9。

提示：在 __next__() 中每次增加 step。注意 step 可能是负数，
此时应该从 start 递减到大于 end。
"""


class StepRange:
    """带步长的范围迭代器。

    >>> list(StepRange(0, 10, 3))
    [0, 3, 6, 9]
    >>> list(StepRange(5, 0, -1))
    [5, 4, 3, 2, 1]
    >>> list(StepRange(0, 5, 1))
    [0, 1, 2, 3, 4]
    >>> list(StepRange(0, 0, 1))
    []
    >>> list(StepRange(10, 0, -3))
    [10, 7, 4, 1]
    """

    def __init__(self, start: int, end: int, step: int = 1) -> None:
        raise NotImplementedError("代码未实现")

    def __iter__(self):
        raise NotImplementedError("代码未实现")

    def __next__(self) -> int:
        raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
