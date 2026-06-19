"""目标：定义一个函数 area(width, height=10)，计算矩形的面积。

提示：参数默认值在参数列表中用 = 指定。当不传 height 时，应使用默认值 10。
"""


def area(width, height=10):
    """计算矩形的面积。

    >>> area(5)
    50
    >>> area(5, 20)
    100
    >>> area(3, 7)
    21
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
