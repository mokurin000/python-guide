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

* [ ] `def`
* [ ] 参数默认值
* [ ] 返回值
  * [ ] `tuple`: 返回多个值
* [ ] 作用域

* [ ] 递归
  * [ ] 递归终止条件
  * [ ] 调用栈
  * [ ] 递归与迭代

### Day 6：错误处理

* [ ] `try...except`
  * [ ] `EOFError`
  * [ ] `ValueError`
* [ ] `raise`

### Day 7：对象与类

* [ ] 对象
* [ ] `id()`
* [ ] `is`
* [ ] `isinstance()`

* [ ] `class`
  * [ ] `self`
  * [ ] `__init__`
  * [ ] 实例方法
  * [ ] 类变量 v.s. 实例变量

* [ ] 继承
  * [ ] `issubclass()`

* [ ] 特殊方法
  * [ ] `__str__`
  * [ ] `__repr__`

* [ ] 附录: Protocol v.s. ABC
  * [ ] `__subclasshook__()`

### Day 8：迭代器与生成器

* [ ] 可迭代对象
* [ ] `list()`
* [ ] 迭代器
* [ ] `iter()`
* [ ] `next()`
* [ ] `StopIteration`

* [ ] 实现迭代器
  * [ ] `__iter__()`
  * [ ] `__next__()`

* [ ] 生成器
  * [ ] 生成器函数
    * [ ] `yield`
  * [ ] 生成器推导式

### Day 9：函数式编程

* [ ] `lambda`
* [ ] `map()`
* [ ] `filter()`
* [ ] `functools.reduce()`
* [ ] `functools.partial()`

### Day 10：模块与项目

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

### Day 11：文件读写

* [ ] `open()`
* [ ] `read()`
* [ ] `write()`
* [ ] `with`
* [ ] 文本模式与二进制模式

* [ ] `pathlib`
* [ ] `json`

### 附录：进阶 Python

* [ ] 函数装饰器

* [ ] `contextlib.AbstractContextManager`
  * [ ] `__enter__()`
  * [ ] `__exit__()`
