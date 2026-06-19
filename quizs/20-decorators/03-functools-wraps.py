"""目标：使用 functools.wraps 保留装饰后函数的元数据。

实现装饰器，在不使用和使用 @wraps 两种情况下观察区别。
最终版本的 decorator 应该使用 @wraps 保留原始函数的元数据。

提示：
- `functools.wraps` 是一个装饰器，用于 wrapper 函数
- 它复制 __name__、__doc__、__module__ 等属性
- 使用 `@wraps(func)` 放在 wrapper 函数定义之上
"""

from functools import wraps


def bad_logger(func):
    """装饰器：不保留元数据（用于对比）。"""
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


def good_logger(func):
    '''装饰器：使用 @wraps 保留元数据。

    >>> @good_logger
    ... def greet(name):
    ...     """向某人问好。"""
    ...     return f"你好, {name}!"
    ...
    >>> greet.__name__
    'greet'
    >>> greet.__doc__
    '向某人问好。'
    >>> result = greet("Alice")
    调用 greet
    >>> result
    '你好, Alice!'

    >>> @good_logger
    ... def add(a, b):
    ...     return a + b
    ...
    >>> add.__name__
    'add'
    >>> add(3, 5)
    调用 add
    8
    '''
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
