"""目标：实现带参数的装饰器。

创建一个 repeat(n) 装饰器，让被装饰的函数重复执行 n 次，
并返回所有结果的列表。

提示：
- 带参数的装饰器需要三层嵌套：
  1. 最外层接收装饰器参数（如 n）
  2. 第二层接收被装饰函数 func
  3. 第三层是 wrapper，接收调用参数
- 使用 @wraps 保留元数据
"""

from functools import wraps


def repeat(n: int):
    """装饰器：将被装饰函数重复执行 n 次，返回结果列表。

    >>> @repeat(3)
    ... def say(message):
    ...     return f"说: {message}"
    ...
    >>> say("你好")
    ['说: 你好', '说: 你好', '说: 你好']

    >>> @repeat(1)
    ... def greet(name):
    ...     return f"你好, {name}!"
    ...
    >>> greet("Alice")
    ['你好, Alice!']

    >>> @repeat(0)
    ... def nothing():
    ...     return 42
    ...
    >>> nothing()
    []

    >>> @repeat(3)
    ... def add(a, b):
    ...     return a + b
    ...
    >>> add.__name__
    'add'
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
