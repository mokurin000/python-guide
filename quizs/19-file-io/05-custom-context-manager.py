"""目标：实现自定义上下文管理器，理解 __enter__ 和 __exit__ 协议。

实现一个文件计数器上下文管理器，模拟统计文件中有多少行。

提示：
- `__enter__(self)` 返回 self 或资源对象
- `__exit__(self, exc_type, exc_val, exc_tb)` 执行清理
- `__exit__` 返回 False 让异常继续传播，或返回 True 吞没异常
- 可以继承 `contextlib.AbstractContextManager`
"""


class LineCounter:
    """上下文管理器：进入时记录开始状态，退出时打印统计信息。

    模拟统计文件行数的上下文管理器。

    >>> with LineCounter("test") as lc:
    ...     lc.add_line("hello")
    ...     lc.add_line("world")
    ...
    >>> lc.count
    2

    >>> with LineCounter("empty") as lc:
    ...     pass
    ...
    >>> lc.count
    0
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.count = 0

    def __enter__(self):
        """返回 self 以便在 with 块中访问。"""
        raise NotImplementedError("代码未实现")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """打印文件名和行数统计，清理资源。"""
        raise NotImplementedError("代码未实现")

    def add_line(self, line: str) -> None:
        """增加一行计数。"""
        self.count += 1


class SafeDivision:
    """上下文管理器：在 with 块中执行除法操作，捕获 ZeroDivisionError。

    这个上下文管理器模拟"安全除法"——除零时吞没异常并记录。

    >>> with SafeDivision() as sd:
    ...     sd.divide(10, 2)
    ...
    5.0
    >>> with SafeDivision() as sd:
    ...     sd.divide(10, 0)
    ...
    除数不能为零！已记录。
    >>> sd.error_occurred
    True

    >>> with SafeDivision() as sd:
    ...     sd.divide(10, 3)
    ...
    3.3333333333333335
    >>> sd.error_occurred
    False
    """

    def __init__(self) -> None:
        self.error_occurred = False

    def __enter__(self):
        raise NotImplementedError("代码未实现")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """如果异常是 ZeroDivisionError，吞没它并打印提示。"""
        raise NotImplementedError("代码未实现")

    def divide(self, a: float, b: float) -> float:
        """执行除法，如果出错则让异常传播到 __exit__。"""
        return a / b


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
