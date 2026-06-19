"""目标：定义 Animal 基类及 Dog、Cat 子类，演示继承和方法覆盖。
实现一个函数 animal_sound(animal)，利用多态返回不同动物的叫声。

提示：class Dog(Animal): 表示 Dog 继承自 Animal。
super().__init__(name) 可以调用父类的 __init__ 方法。
子类可以覆盖（override）父类的方法。
issubclass(子类, 父类) 检查继承关系。
"""


class Animal:
    """动物基类。

    >>> a = Animal("未知动物")
    >>> a.name
    '未知动物'
    >>> a.speak()
    '...'
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        """返回动物的叫声，基类默认返回 '...'。"""
        raise NotImplementedError("代码未实现")


class Dog(Animal):
    """狗，继承自动物。

    >>> dog = Dog("旺财")
    >>> dog.name
    '旺财'
    >>> dog.speak()
    '汪汪！'
    """

    def speak(self) -> str:
        raise NotImplementedError("代码未实现")


class Cat(Animal):
    """猫，继承自动物。

    >>> cat = Cat("咪咪")
    >>> cat.name
    '咪咪'
    >>> cat.speak()
    '喵喵！'
    """

    def speak(self) -> str:
        raise NotImplementedError("代码未实现")


class LoudDog(Dog):
    """大嗓门的狗，继承自 Dog，叫声重复三遍。

    >>> ld = LoudDog("大嗓门")
    >>> ld.speak()
    '汪汪！汪汪！汪汪！'
    """

    def speak(self) -> str:
        raise NotImplementedError("代码未实现")


def animal_sound(animal: Animal) -> str:
    """返回动物的自我介绍，格式为 "{name} 说：{叫声}"。

    >>> animal_sound(Dog("旺财"))
    '旺财 说：汪汪！'
    >>> animal_sound(Cat("咪咪"))
    '咪咪 说：喵喵！'
    >>> animal_sound(Animal("未知"))
    '未知 说：...'
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
