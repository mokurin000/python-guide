"""目标：实现 CountUp 类，使其成为一个迭代器，从 start 计数到 end-1。

例如 CountUp(3, 6) 依次产生 3, 4, 5。

提示：在类中定义 __iter__() 和 __next__() 方法。
当计数达到 end 时，__next__() 应抛出 StopIteration。
"""


class CountUp:
    """从 start 迭代到 end-1 的迭代器。

    >>> c = CountUp(3, 6)
    >>> list(c)
    [3, 4, 5]
    >>> list(CountUp(0, 5))
    [0, 1, 2, 3, 4]
    >>> list(CountUp(5, 5))
    []
    >>> list(CountUp(0, 1))
    [0]
    """

    def __init__(self, start: int, end: int) -> None:
        raise NotImplementedError("代码未实现")

    def __iter__(self):
        raise NotImplementedError("代码未实现")

    def __next__(self) -> int:
        raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
