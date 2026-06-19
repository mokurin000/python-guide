"""目标：实现 take(iterable, n) 函数，返回可迭代对象的前 n 个元素组成的列表。

提示：用 iter() 从 iterable 获取迭代器，然后用 next() 逐个取值。
捕获 StopIteration 以处理可迭代对象元素不足 n 个的情况。
"""


def take(iterable, n: int) -> list:
    """返回可迭代对象的前 n 个元素。

    >>> take([10, 20, 30, 40, 50], 3)
    [10, 20, 30]
    >>> take("hello", 2)
    ['h', 'e']
    >>> take([1, 2, 3], 5)
    [1, 2, 3]
    >>> take(range(100, 105), 3)
    [100, 101, 102]
    >>> take([], 3)
    []
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
