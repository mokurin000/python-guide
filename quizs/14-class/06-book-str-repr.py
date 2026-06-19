"""目标：定义一个 Book 类，实现 __str__ 和 __repr__ 特殊方法。

提示：
- __str__ 返回用户友好的字符串描述，由 print() 和 str() 调用。
- __repr__ 返回开发者友好的表示，通常包含能重建对象的信息。
- __repr__ 中的 {self.title!r} 会使用 repr(self.title) 获得带引号的字符串。
- 如果只有 __repr__ 没有 __str__，print() 会退而使用 __repr__。
"""


class Book:
    """表示一本书。

    >>> b = Book("Python 入门", "张三", 2024)
    >>> print(b)  # __str__
    《Python 入门》——张三 (2024)
    >>> repr(b)   # __repr__
    "Book('Python 入门', '张三', 2024)"
    >>> b2 = Book("数据结构", "李四", 2023)
    >>> print(b2)
    《数据结构》——李四 (2023)
    """

    def __init__(self, title: str, author: str, year: int) -> None:
        raise NotImplementedError("代码未实现")

    def __str__(self) -> str:
        """返回格式：《书名》——作者 (年份)"""
        raise NotImplementedError("代码未实现")

    def __repr__(self) -> str:
        """返回格式：Book('书名', '作者', 年份)"""
        raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
