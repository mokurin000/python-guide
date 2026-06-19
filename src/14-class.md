# 对象与类

在之前的章节中，我们学习了 `int`、`str`、`list`、`dict` 等数据类型，以及如何定义函数、处理错误。你可能已经注意到，这些类型似乎各自拥有一些"方法"——比如 `"hello".upper()`、`[1, 2, 3].append(4)`。这些方法是从哪里来的？我们能不能也创建自己的类型，让它拥有自己的方法？

答案是肯定的——通过**类 (class)**。

## 对象

> **对象 (Object)** 是 Python 中一切数据的核心概念。每个值——无论是数字、字符串、列表还是函数——都是一个对象。

在 Python 的世界里，"万物皆对象"。每个对象都有三个基本特征：

1. **身份 (Identity)** —— 对象在内存中的唯一标识
2. **类型 (Type)** —— 对象属于哪个类
3. **值 (Value)** —— 对象存储的数据

### `id()` —— 对象的唯一标识

`id()` 函数返回对象的**唯一标识**，可以理解为对象在内存中的地址：

```python
>>> a = "hello"
>>> b = "hello"
>>> id(a)
140234567890432  # 你的运行结果可能不同
>>> id(b)
140234567890432  # 与 a 相同——Python 可能会复用相同的小字符串对象
```

> Python 会对某些不可变对象（如小整数、短字符串）进行**驻留 (interning)** 优化，使相同值的对象共享同一内存地址。但这是一种实现细节，不应依赖。

```python
>>> x = 256
>>> y = 256
>>> id(x) == id(y)
True
>>> x = 257
>>> y = 257
>>> id(x) == id(y)  # 大整数不驻留
False
```

### `is` —— 比较对象身份

`is` 操作符用于判断两个变量是否引用**同一个对象**，即比较它们的 `id()` 是否相等：

```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a == b      # == 比较值
True
>>> a is b      # is 比较身份（是否同一个对象）
False
>>> c = a
>>> c is a      # c 和 a 引用同一个对象
True
```

> **不要混淆 `==` 和 `is`**：`==` 比较**值**，`is` 比较**身份**。大多数情况下你需要的是 `==`。`is` 的常见用途是比较 `None`：`x is None` 或 `x is not None`。

### 可变对象默认值的陷阱

在 [函数与递归](./12-function.md) 一章中，我们提到过"不要用可变类型作为默认值"。现在我们可以用 `is` 来理解为什么：

```python
>>> def add_item(item, lst=[]):  # 默认值在函数定义时计算
...     lst.append(item)
...     return lst
...
>>> add_item(1)
[1]
>>> add_item(2)  # 同一个列表对象！
[1, 2]
>>> add_item(3)  # 还是同一个！
[1, 2, 3]
```

默认列表 `[]` 只在**函数定义时创建一次**，之后每次调用都在修改同一个列表对象。可以用 `id()` 验证：

```python
>>> id(add_item.__defaults__[0])
140234567890432  # 始终相同
```

> 正确的做法是使用 `None` 作为默认值，在函数内部创建一个新列表：

```python
>>> def add_item(item, lst=None):
...     if lst is None:
...         lst = []
...     lst.append(item)
...     return lst
...
>>> add_item(1)
[1]
>>> add_item(2)  # 每次都是新列表
[2]
```

### `isinstance()` —— 检查类型

`isinstance()` 函数用于检查一个对象是否属于某个类型（或类型元组中的任意一个）：

```python
>>> isinstance(42, int)
True
>>> isinstance("hello", str)
True
>>> isinstance([1, 2], list)
True
>>> isinstance(42, (int, float, str))  # 检查多个类型
True
```

`isinstance()` 也支持继承关系（我们稍后会讲到），所以它比 `type(obj) == int` 更灵活、更推荐。

## 定义类

> **类 (Class)** 是创建对象的模板。它定义了对象拥有哪些属性（变量）和方法（函数）。

我们可以把类比作"饼干模具"，对象就是通过这个模具制作出来的"饼干"。

### 基本语法

使用 `class` 关键字定义一个类：

```python
class 类名:
    """类的文档字符串"""
    pass
```

来看一个最简单的例子——定义一个 `Dog` 类：

```python
>>> class Dog:
...     pass
...
>>> d = Dog()  # 创建（实例化）一个 Dog 对象
>>> type(d)
<class '__main__.Dog'>
>>> isinstance(d, Dog)
True
```

### `__init__` —— 构造方法

> **`__init__`** 是一个**特殊方法 (special method)**，在创建对象时自动调用，用于初始化对象的属性。

它的名称以双下划线开头和结尾（因此也被称为 "dunder method"），Python 会在特定时机自动调用这些方法。

```python
>>> class Dog:
...     def __init__(self, name, age):
...         self.name = name   # 实例变量
...         self.age = age
...
>>> my_dog = Dog("旺财", 3)
>>> my_dog.name
'旺财'
>>> my_dog.age
3
```

### `self` —— 实例引用

> **`self`** 指向当前正在操作的对象实例。在定义实例方法时，`self` 必须是第一个参数。

```python
>>> class Dog:
...     def __init__(self, name):
...         self.name = name
...
...     def introduce(self):
...         return f"我是{self.name}！"
...
>>> d = Dog("旺财")
>>> d.introduce()  # Python 自动将 d 作为 self 传入
'我是旺财！'
>>> Dog.introduce(d)  # 也可以这样显式调用
'我是旺财！'
```

当调用 `d.introduce()` 时，Python 自动将 `d` 作为第一个参数（即 `self`）传入。`self` 这个名字是约定俗成的，但理论上可以使用任何名称——不过请务必使用 `self`，这是 Python 社区的通用规范。

### 实例方法

在类中定义的函数就是**实例方法 (instance method)**，它们通过 `self` 访问实例的属性：

```python
>>> class Rectangle:
...     def __init__(self, width, height):
...         self.width = width
...         self.height = height
...
...     def area(self):
...         return self.width * self.height
...
...     def perimeter(self):
...         return 2 * (self.width + self.height)
...
>>> r = Rectangle(3, 4)
>>> r.area()
12
>>> r.perimeter()
14
```

### 类变量 vs 实例变量

> **类变量 (class variable)** 在类体内直接定义，被所有实例共享。**实例变量 (instance variable)** 在 `__init__` 中用 `self.xxx` 定义，每个实例独立拥有。

```python
>>> class Student:
...     school = "编程中学"       # 类变量——所有学生共享
...
...     def __init__(self, name):
...         self.name = name     # 实例变量——每个学生独有
...
>>> s1 = Student("小明")
>>> s2 = Student("小红")
>>> s1.name
'小明'
>>> s2.name
'小红'
>>> Student.school  # 通过类访问
'编程中学'
>>> s1.school       # 实例可以访问类变量
'编程中学'
>>> s2.school
'编程中学'
```

#### 修改类变量 vs 实例变量

```python
>>> Student.school = "新编程中学"  # 修改类变量
>>> s1.school
'新编程中学'
>>> s2.school
'新编程中学'
```

如果通过实例赋值，会创建同名的**实例变量**，覆盖类变量：

```python
>>> s1.school = "其他学校"  # 创建实例变量，不修改类变量
>>> s1.school
'其他学校'
>>> Student.school  # 类变量不变
'新编程中学'
>>> s2.school       # 其他实例不受影响
'新编程中学'
```

> 在实例上读取属性时，Python 先查找实例变量，找不到再查找类变量。但**赋值**总是创建或修改实例变量，不会影响类变量。

## 继承

> **继承 (Inheritance)** 允许我们基于现有类创建新类，复用和扩展已有功能。

### 基本继承

```python
class 子类名(父类名):
    ...
```

```python
>>> class Animal:
...     def __init__(self, name):
...         self.name = name
...
...     def speak(self):
...         return "..."
...
>>> class Dog(Animal):      # Dog 继承自 Animal
...     def speak(self):     # 覆盖父类方法
...         return "汪汪！"
...
>>> class Cat(Animal):      # Cat 也继承自 Animal
...     def speak(self):
...         return "喵喵！"
...
>>> animals = [Dog("旺财"), Cat("咪咪"), Animal("未知")]
>>> for a in animals:
...     print(f"{a.name} 说：{a.speak()}")
...
旺财 说：汪汪！
咪咪 说：喵喵！
未知 说：...
```

这就是**多态 (Polymorphism)**——不同的子类以不同的方式实现同一个方法。

### `issubclass()`

`issubclass()` 用于检查一个类是否是另一个类的子类：

```python
>>> issubclass(Dog, Animal)
True
>>> issubclass(Cat, Animal)
True
>>> issubclass(Dog, Cat)
False
>>> issubclass(Animal, object)  # 所有类都继承自 object
True
```

### `super()` —— 调用父类方法

在子类中，可以使用 `super()` 来调用父类的方法：

```python
>>> class Puppy(Dog):
...     def __init__(self, name, toy):
...         super().__init__(name)  # 调用 Dog 的 __init__
...         self.toy = toy
...
...     def play(self):
...         return f"{self.name} 在玩 {self.toy}"
...
>>> p = Puppy("小黄", "球")
>>> p.speak()       # 继承自 Dog
'汪汪！'
>>> p.play()
'小黄 在玩 球'
```

### 方法覆盖 (Override)

子类可以完全**覆盖 (override)** 父类的方法，也可以使用 `super()` 扩展父类方法：

```python
>>> class LoudDog(Dog):
...     def speak(self):
...         return super().speak() * 3  # 在父类方法基础上扩展
...
>>> ld = LoudDog("大嗓门")
>>> ld.speak()
'汪汪！汪汪！汪汪！'
```

## 特殊方法

> **特殊方法 (Special Methods)** 以双下划线开头和结尾，让自定义类能够与 Python 的内置操作无缝协作。

### `__str__` 与 `__repr__`

这两个方法都用于返回对象的字符串表示，但用途不同：

- **`__str__`**：面向用户的友好描述，由 `print()` 和 `str()` 调用
- **`__repr__`**：面向开发者的详细描述，由交互式解释器自动调用，通常返回能重建对象的表达式

```python
>>> class Book:
...     def __init__(self, title, author):
...         self.title = title
...         self.author = author
...
...     def __str__(self):
...         return f"《{self.title}》——{self.author}"
...
...     def __repr__(self):
...         return f"Book({self.title!r}, {self.author!r})"
...
>>> b = Book("Python 入门", "张三")
>>> print(b)        # 调用 __str__
《Python 入门》——张三
>>> b               # 交互式解释器调用 __repr__
Book('Python 入门', '张三')
```

> 如果类只定义了 `__repr__` 而没有定义 `__str__`，那么 `print()` 会退而使用 `__repr__`。因此，一个好的做法是至少实现 `__repr__`。

### 更多特殊方法

Python 中还有大量特殊方法，可以让自定义类支持各种操作：

| 特殊方法      | 作用         | 触发方式       |
| ------------- | ------------ | -------------- |
| `__len__`     | 返回长度     | `len(obj)`     |
| `__eq__`      | 相等比较     | `obj == other` |
| `__lt__`      | 小于比较     | `obj < other`  |
| `__add__`     | 加法         | `obj + other`  |
| `__getitem__` | 索引访问     | `obj[key]`     |
| `__call__`    | 使对象可调用 | `obj()`        |

我们将在后续章节中逐步认识它们。

## 附录: Protocol vs ABC

Python 中定义接口有两种不同的哲学：

### 鸭子类型与 Protocol

> **鸭子类型 (Duck Typing)** 的核心思想是："如果它走起来像鸭子，叫起来像鸭子，那它就是鸭子。"

在鸭子类型下，我们不关心对象的**具体类型**，只关心它**有没有实现所需的方法**：

```python
>>> class Duck:
...     def quack(self):
...         return "嘎嘎！"
...
>>> class Person:
...     def quack(self):
...         return "我在学鸭子叫！"
...
>>> def make_quack(obj):
...     return obj.quack()  # 不检查类型，只管调用
...
>>> make_quack(Duck())
'嘎嘎！'
>>> make_quack(Person())
'我在学鸭子叫！'
```

Python 3.8+ 引入了 `typing.Protocol` 来显式定义这样的接口：

```python
>>> from typing import Protocol
...
>>> class Quackable(Protocol):
...     def quack(self) -> str: ...
...
>>> def make_quack(obj: Quackable) -> str:
...     return obj.quack()
...
>>> make_quack(Duck())     # 无需显式继承
'嘎嘎！'
>>> make_quack(Person())   # Person 自动符合 Protocol
'我在学鸭子叫！'
```

### ABC (Abstract Base Class)

> **抽象基类 (Abstract Base Class)** 要求子类**必须显式继承**并实现指定的抽象方法。

```python
>>> from abc import ABC, abstractmethod
...
>>> class Animal(ABC):
...     @abstractmethod
...     def speak(self) -> str:
...         pass
...
>>> class Cat(Animal):
...     def speak(self) -> str:
...         return "喵喵！"
...
>>> class Dog(Animal):
...     def speak(self) -> str:
...         return "汪汪！"
...
```

如果尝试实例化没有实现抽象方法的子类，会直接报错：

```python
>>> class IncompleteAnimal(Animal):
...     pass
...
>>> try:
...     obj = IncompleteAnimal()
... except TypeError as e:
...     print(e)
...
Can't instantiate abstract class IncompleteAnimal with abstract method speak
```

### `__subclasshook__()`

`__subclasshook__()` 允许自定义 `issubclass()` 和 `isinstance()` 的行为。结合 ABC，可以实现类似 Protocol 的结构子类型检查：

```python
>>> class Quackable(ABC):
...     @classmethod
...     def __subclasshook__(cls, C):
...         if any("quack" in B.__dict__ for B in C.__mro__):
...             return True
...         return NotImplemented
...
>>> class MyDuck:  # 没有显式继承 Quackable
...     def quack(self):
...         return "嘎！"
...
>>> issubclass(MyDuck, Quackable)  # 但仍然被认为是子类
True
>>> isinstance(MyDuck(), Quackable)
True
```

> 在大多数日常编程中，你不需要直接使用 `__subclasshook__`。理解它有助于深入理解 Python 的类型系统。

## 练习

完成 `quizs/14-class/*.py`。

你可以直接使用 `▷` 运行对应程序，检查是否通过了测试。

同时，标准答案将不再提供。
