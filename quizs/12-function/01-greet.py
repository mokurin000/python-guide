"""目标：定义一个函数 greet(name)，返回个性化的问候语。

提示：函数用 def 关键字定义，用 return 返回值。字符串可以用 + 或 f-string 拼接。
"""


def greet(name):
    """返回问候语。

    >>> greet("小明")
    '你好，小明！'
    >>> greet("Python")
    '你好，Python！'
    >>> greet("世界")
    '你好，世界！'
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
