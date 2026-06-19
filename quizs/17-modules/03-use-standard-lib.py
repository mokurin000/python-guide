"""目标：使用标准库模块 math 和 sys 解决实际问题。

Python 的标准库提供了丰富的功能。本练习将使用 math 和 sys 模块。
"""

import math
import sys


def circle_area(radius: float) -> float:
    """计算圆的面积（使用 math.pi）。

    >>> round(circle_area(1), 4)
    3.1416
    >>> circle_area(0)
    0.0
    """
    raise NotImplementedError("代码未实现")


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """计算两点之间的欧几里得距离（使用 math.sqrt）。

    >>> distance(0, 0, 3, 4)
    5.0
    >>> distance(1, 1, 1, 1)
    0.0
    """
    raise NotImplementedError("代码未实现")


def get_python_version() -> str:
    """返回当前 Python 版本的主版本号.次版本号（使用 sys.version_info）。

    sys.version_info 是一个命名元组，包含 (major, minor, micro, ...)。
    只返回 "主版本.次版本" 格式的字符串。

    >>> import sys
    >>> expected = f"{sys.version_info.major}.{sys.version_info.minor}"
    >>> get_python_version() == expected
    True
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
