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

* [ ] `list`
* [ ] `dict`
* [ ] `set`

### Day 4：循环与遍历

* [ ] `for`
* [ ] `range(end)`
* [ ] `range(start, end, step=1)`
* [ ] 遍历 `list`
* [ ] 遍历 `set`/`dict`

### Day 5：函数

* [ ] `def`
* [ ] 参数默认值
* [ ] 返回值
* [ ] 作用域

### Day 6：错误处理

* [ ] `try...except`
  * [ ] `EOFError`
  * [ ] `ValueError`
* [ ] `raise`

### Day 7：对象与类

* [ ] 对象
* [ ] `id()`
* [ ] `is`
* [] `issubclass()`
* [] `isinstance()`

* [ ] `class`
  * [ ] `self`
  * [ ] `__init__`
  * [ ] 实例方法
  * [ ] 特殊方法
    * [ ] `__str__`
    * [ ] `__repr__`

### Day 8：迭代器与生成器

* [ ] 可迭代对象
  * [ ] `iter()`
* [ ] 迭代器
  * [ ] `next()`
  * [ ] `StopIteration`
* [ ] 实现迭代器
  * [ ] `__iter__()`
  * [ ] `__next__()`
* [ ] 生成器
  * [ ] `yield`
* [ ] 推导式
  * [ ] 列表推导式
  * [ ] 字典推导式
  * [ ] 集合推导式

### Day 9：函数式编程

* [ ] `lambda`
* [ ] `map()`
* [ ] `filter()`
* [ ] `functools.reduce()`
* [ ] `functools.partial()`

### Day 10：文件读写

* [ ] `open()`
* [ ] `read()`
* [ ] `readline()`
* [ ] `readlines()`
* [ ] `write()`
* [ ] `with`
* [ ] 文本模式与二进制模式

### Day 11：模块与项目

* [ ] `import`
* [ ] `from ... import ...`

* [ ] `__name__`
* [ ] `if __name__ == "__main__"`

* [ ] 创建模块
* [ ] 模块搜索路径

* [ ] 创建包（Package）

* [ ] `uv`
  * [ ] 创建项目
  * [ ] 虚拟环境
  * [ ] 安装依赖

### Day 12：进阶 Python

* [ ] Protocol v.s. ABC
  * [ ] `__subclasshook__()`

* [ ] 函数装饰器

* [ ] `contextlib.AbstractContextManager`
  * [ ] `__enter__()`
  * [ ] `__exit__()`
