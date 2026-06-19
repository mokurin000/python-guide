"""目标：定义一个 Dog 类，包含 __init__ 方法和 bark() 实例方法。

提示：使用 class 关键字定义类。__init__ 是构造方法，在创建对象时自动调用，
用于初始化属性。self 指向当前实例，是所有实例方法的第一个参数。
"""


class Dog:
    """表示一只狗。

    >>> dog = Dog("旺财", 3)
    >>> dog.name
    '旺财'
    >>> dog.age
    3
    >>> dog.bark()
    '旺财说：汪汪！'
    >>> dog2 = Dog("小白", 1)
    >>> dog2.bark()
    '小白说：汪汪！'
    """

    def __init__(self, name: str, age: int) -> None:
        raise NotImplementedError("代码未实现")

    def bark(self) -> str:
        """
        返回狗的叫声，格式为 "{name}说：汪汪！"
        """
        raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
