"""目标：实现一个计时装饰器。

创建一个装饰器 timer，测量函数的执行时间并打印。
由于 doctest 很难测试精确的时间，我们使用一个简单的断言：
装饰后的函数返回值保持不变。

提示：
- 在 wrapper 中记录开始时间 `time.time()`
- 执行原函数得到结果
- 记录结束时间，计算差值
- 打印耗时信息，返回结果
- 注意使用 `functools.wraps` 保留元数据
"""

import time
from functools import wraps


def timer(func):
    """装饰器：测量函数执行时间并打印。

    >>> @timer
    ... def slow_sum(n):
    ...     return sum(range(n))
    ...
    >>> result = slow_sum(1000)
    slow_sum 耗时: ...秒
    >>> result
    499500

    >>> @timer
    ... def fast_add(a, b):
    ...     return a + b
    ...
    >>> fast_add(3, 5)
    fast_add 耗时: ...秒
    8
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
