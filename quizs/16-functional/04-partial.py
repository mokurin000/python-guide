"""目标：使用 functools.partial() 创建偏函数。

实现以下函数，使用 `partial(func, *args, **kwargs)` 固定部分参数，
创建更特化的函数版本。

提示：
- `partial(func, arg)` 固定 func 的第一个位置参数
- `partial(func, keyword=value)` 固定 func 的关键字参数
- 偏函数返回的是一个可调用的新函数
"""

from functools import partial


def create_power_function(exp: int):
    """返回一个计算 base ** exp 的偏函数。

    >>> square = create_power_function(2)
    >>> square(5)
    25
    >>> cube = create_power_function(3)
    >>> cube(4)
    64
    """
    raise NotImplementedError("代码未实现")


def create_discount_function(discount_rate: float):
    """返回一个计算打折后价格的偏函数。
    原函数为 `def get_price(original_price, discount_rate): ...`，
    你需要用 partial 固定 discount_rate。

    >>> ten_percent_off = create_discount_function(0.1)
    >>> ten_percent_off(100)
    90.0
    >>> half_off = create_discount_function(0.5)
    >>> half_off(200)
    100.0
    """
    raise NotImplementedError("代码未实现")


def create_base_logarithm(base: float):
    """返回一个计算以 base 为底的对数的偏函数。
    使用 `math.log(x, base)`。

    >>> log10 = create_base_logarithm(10)
    >>> round(log10(100), 4)
    2.0
    >>> ln = create_base_logarithm(2.718281828459045)
    >>> round(ln(10), 4)
    2.3026
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
