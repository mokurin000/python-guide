"""目标：实现一个简单的日志装饰器。

创建一个装饰器 logger，在调用函数时打印 "调用 <函数名>()"，
在函数返回时打印 "返回: <返回值>"。

提示：
- 装饰器的参数是函数 func，返回值是新函数 wrapper
- wrapper 使用 *args, **kwargs 接受任意参数
- 调用原函数前/后添加打印语句
"""


def logger(func):
    """装饰器：在函数调用前后打印日志。

    >>> @logger
    ... def greet(name):
    ...     return f"你好, {name}!"
    ...
    >>> result = greet("Alice")
    调用 greet()
    返回: 你好, Alice!
    >>> result
    '你好, Alice!'

    >>> @logger
    ... def add(a, b):
    ...     return a + b
    ...
    >>> add(3, 5)
    调用 add()
    返回: 8
    8
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
