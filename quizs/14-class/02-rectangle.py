"""目标：定义一个 Rectangle 类，支持计算面积 (area) 和周长 (perimeter)。

提示：在 __init__ 中接收 width 和 height。实例方法通过 self 访问实例变量。
"""


class Rectangle:
    """表示一个矩形。

    >>> r = Rectangle(3, 4)
    >>> r.width
    3
    >>> r.height
    4
    >>> r.area()
    12
    >>> r.perimeter()
    14
    >>> r2 = Rectangle(5, 5)
    >>> r2.area()
    25
    >>> r2.perimeter()
    20
    """

    def __init__(self, width: float, height: float) -> None:
        raise NotImplementedError("代码未实现")

    def area(self) -> float:
        """返回矩形的面积（宽 × 高）。"""
        raise NotImplementedError("代码未实现")

    def perimeter(self) -> float:
        """返回矩形的周长（2 × (宽 + 高)）。"""
        raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
