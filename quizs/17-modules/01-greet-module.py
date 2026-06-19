"""目标：创建一个模块并理解 __name__ 的行为。

在 Python 中，每个模块都有一个内置的 __name__ 属性：
- 当模块直接运行时，__name__ 为 "__main__"
- 当模块被导入时，__name__ 为模块的文件名（不含 .py）

请实现以下函数，模拟模块的 __name__ 行为判断逻辑。
"""


def is_run_directly(name: str) -> bool:
    """判断给定的 __name__ 值是否表示模块被直接运行。

    >>> is_run_directly("__main__")
    True
    >>> is_run_directly("greet")
    False
    >>> is_run_directly("math")
    False
    """
    raise NotImplementedError("代码未实现")


def greet(name: str) -> str:
    """返回问候语。

    >>> greet("世界")
    '你好，世界！'
    >>> greet("Python")
    '你好，Python！'
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
