"""目标：实现几个函数，练习 id()、is 操作符和 isinstance() 的使用。

提示：
- id(obj) 返回对象的唯一标识（CPython中是它的内存地址）。
- obj is other 等价于 id(obj) == id(other)，判断是否同一个对象。
- isinstance(obj, type) 检查对象是否属于某类型。
"""


def is_same_object(a, b) -> bool:
    """判断 a 和 b 是否引用同一个对象。

    >>> is_same_object([1, 2, 3], [1, 2, 3])
    False
    >>> x = [1, 2, 3]
    >>> is_same_object(x, x)
    True
    >>> is_same_object(None, None)
    True
    """
    raise NotImplementedError("代码未实现")


def is_integer_or_float(obj) -> bool:
    """判断 obj 是否是 int 或 float 类型。

    >>> is_integer_or_float(42)
    True
    >>> is_integer_or_float(3.14)
    True
    >>> is_integer_or_float("hello")
    False
    >>> is_integer_or_float([1, 2])
    False
    """
    raise NotImplementedError("代码未实现")


def count_unique_objects(*args) -> int:
    """返回参数列表中不同对象的数量（基于 id 判断，而非值相等）。

    >>> a = [1, 2]
    >>> b = [1, 2]
    >>> c = a
    >>> count_unique_objects(a, b, c)
    2
    >>> count_unique_objects(1, 2, 3)
    3
    >>> x = {"key": "value"}
    >>> count_unique_objects(x, x, x)
    1
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
