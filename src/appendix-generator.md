# 附录：生成器高级方法

生成器对象除了支持 `next()` 之外，还额外提供了三个方法，用于在运行中与生成器交互。

### `.close()` —— 关闭生成器

`close()` 在生成器暂停的 `yield` 处注入 `GeneratorExit` 异常，强制生成器退出。如果生成器内部捕获了 `GeneratorExit`，必须重新抛出或直接返回，否则会报错：

```python
>>> def count_down(n):
...     try:
...         while n > 0:
...             yield n
...             n -= 1
...     except GeneratorExit:
...         print("生成器被关闭")
...         raise
...
>>> gen = count_down(3)
>>> next(gen)
3
>>> next(gen)
2
>>> gen.close()
生成器被关闭
```

> 关闭后的生成器不能再使用——任何对它的 `next()` 或 `send()` 调用都会抛出 `StopIteration`。

### `.send()` —— 向生成器发送值

`send(value)` 将值发送给生成器，替代当前的 `yield` 表达式的结果，并让生成器继续执行到下一个 `yield`：

```python
>>> def echo():
...     while True:
...         received = yield
...         print(f"收到：{received}")
...
>>> gen = echo()
>>> next(gen)       # 启动生成器，执行到第一个 yield
>>> gen.send("你好")
收到：你好
>>> gen.send(42)
收到：42
```

> 首次与生成器交互必须使用 `next(gen)` 或 `gen.send(None)` 来启动它，因为第一个 `yield` 之前没有 `yield` 表达式可以接收值。

`send()` 也可以配合返回值的 `yield` 实现协程风格的双向通信：

```python
>>> def accumulator():
...     total = 0
...     while True:
...         value = yield total
...         total += value
...
>>> acc = accumulator()
>>> next(acc)   # 启动，返回初始 total
0
>>> acc.send(10)
10
>>> acc.send(5)
15
>>> acc.send(20)
35
```

### `.throw()` —— 向生成器注入异常

`throw(exc_type)` 在生成器暂停的 `yield` 处抛出一个异常。如果生成器内部捕获了该异常，`throw()` 会返回下一个 `yield` 的值；否则异常会传播给调用者：

```python
>>> def safe_divide():
...     try:
...         while True:
...             x, y = yield
...             yield x / y
...     except ZeroDivisionError:
...         yield "除零错误"
...
>>> gen = safe_divide()
>>> next(gen)         # 启动
>>> gen.send((10, 2)) # 正常计算
5.0
>>> gen.throw(ZeroDivisionError)  # 注入异常
'除零错误'
```

### 小结

| 方法           | 作用                            |
| -------------- | ------------------------------- |
| `.close()`     | 注入 `GeneratorExit` 关闭生成器 |
| `.send(value)` | 向生成器发送值，继续执行        |
| `.throw(exc)`  | 在 `yield` 处注入异常           |

这三个方法在日常开发中不如 `for` 循环和 `next()` 常用，但它们在实现协程、异步编程、以及复杂生成器控制流时非常重要。