"""目标：理解不同导入方式的区别。

Python 提供了多种导入方式：
1. `import module` —— 导入整个模块，通过 module.name 访问
2. `from module import name` —— 只导入特定名称
3. `import module as alias` —— 给模块起别名

请实现以下函数，模拟不同导入方式的行为。
"""

import math


def sqrt_via_import(x: float) -> float:
    """使用 import math 方式计算平方根。

    注意：不能删除文件顶部的 import math，在函数内部使用 math.sqrt。

    >>> sqrt_via_import(16)
    4.0
    >>> sqrt_via_import(9)
    3.0
    """
    raise NotImplementedError("代码未实现")


def ceil_via_import(x: float) -> int:
    """使用 from math import ceil 方式计算向上取整。

    提示：在函数内部使用 from math import ceil，然后调用 ceil。

    >>> ceil_via_import(3.14)
    4
    >>> ceil_via_import(5.99)
    6
    """
    raise NotImplementedError("代码未实现")


def floor_via_alias(x: float) -> int:
    """使用 import math as m 方式计算向下取整。

    提示：在函数内部使用 import math as m，然后通过 m.floor 调用。

    >>> floor_via_alias(3.99)
    3
    >>> floor_via_alias(5.14)
    5
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
