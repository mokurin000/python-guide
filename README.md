# python-guide

面向中文读者的 Python 入门教程。

## 许可证

本书原创文本内容（除代码示例）以外，均以 CC-BY-NC-4.0 协议发布，书中代码与本书源码内附带源码均以 MIT 协议授权。

## Roadmap

### Day 1：基础概念

* [x] 安装 Python
* [x] 数据类型与变量

  * [x] `int`
  * [x] `float`
    * [x] 附录: IEEE 754
  * [x] `str`
  * [x] `bool`
* [x] 输入与输出

  * [x] `input()`
  * [x] `print()`
* [x] 内置函数

### Day 2：控制流程

* [x] `if`
* [x] `while`

### Day 3：数据结构

* [x] `list`
* [x] `dict`
* [x] `set`

### Day 4：循环与遍历

* [x] `for`
* [x] `range()`
* [x] 遍历 `list`
* [x] 遍历 `set`/`dict`

* [x] 列表推导式
* [x] 字典推导式
* [x] 集合推导式

### Day 5：函数与递归

* [x] `def`
* [x] 参数默认值
* [x] 返回值
  * [x] `tuple`: 返回多个值
* [x] 作用域

* [x] 递归
  * [x] 递归终止条件
  * [x] 递归与迭代

* [x] 调用栈

### Day 6：错误处理

* [x] `try...except`
  * [x] `EOFError`
  * [x] `ValueError`
* [x] `raise`

### Day 7：对象与类

* [x] 对象
* [x] `id()`
* [x] `is`
  * [x] 函数可变对象默认值
* [x] `isinstance()`

* [x] `class`
  * [x] `self`
  * [x] `__init__`
  * [x] 实例方法
  * [x] 类变量 v.s. 实例变量

* [x] 继承
  * [x] `issubclass()`

* [x] 特殊方法
  * [x] `__str__`
  * [x] `__repr__`

* [x] 附录: Protocol v.s. ABC
  * [x] `__subclasshook__()`

### Day 8：迭代器与生成器

* [x] 可迭代对象
* [x] `list()`
* [x] 迭代器
* [x] `iter()`
* [x] `next()`
* [x] `StopIteration`

* [x] 实现迭代器
  * [x] `__iter__()`
  * [x] `__next__()`

* [x] 生成器
  * [x] 生成器函数
    * [x] `yield`
  * [x] 生成器推导式

### Day 9：函数式编程

* [x] `lambda`
* [x] `map()`
* [x] `filter()`
* [x] `functools.reduce()`
* [x] `functools.partial()`

### Day 10：模块与项目

* [x] `import`
* [x] `from ... import ...`

* [x] `__name__`
* [x] `if __name__ == "__main__"`

* [x] 创建模块
* [x] 模块搜索路径

* [x] 创建包（Package）

* [x] `uv`
  * [x] 创建项目
  * [x] 虚拟环境（附录）
  * [x] 安装依赖（附录）

### 附录：文件读写

* [x] `open()`
  * [x] Windows: encoding=`utf-8`
* [x] `read()`
* [x] `write()`
* [x] `with`
* [x] 文本模式与二进制模式

* [x] `pathlib`
  * [x] `Path.joinpath`
  * [x] `/`
* [x] `json`
  * [x] load, loads
  * [x] dump, dumps
    * [x] indent=4
    * [x] ensure_ascii=False

### 附录：进阶特性

* [x] 函数装饰器

* [x] `contextlib.AbstractContextManager`
  * [x] `__enter__()`
  * [x] `__exit__()`
