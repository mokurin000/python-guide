# 附录：现代化 Python 生态速览

恭喜你走到这里！在本书中，你已经掌握了 Python 的核心语法、数据结构、函数式编程、模块化、文件读写与装饰器等基本功。但 Python 之所以强大，离不开它背后庞大的第三方库生态。

本章将快速介绍六个当下最活跃、最实用的 Python 库/主题。它们各自解决不同领域的问题——数据验证、Web 开发、数据分析、可视化、异步编程——每个都值得你进一步探索。

> 本章只做"导游式"概览，不深入细节。如有兴趣，请直接打开官网学习。

---

## SQLModel

**[SQLModel](https://sqlmodel.tiangolo.com/)** 是一个用于与数据库交互的 ORM（对象关系映射）库，由 FastAPI 的作者开发。它巧妙地将 **SQLAlchemy** 与 **Pydantic** 融合在一起，让你可以用同一个模型类同时完成数据库表映射和数据校验。

- 使用 Python 类型注解定义数据库表结构
- 自动生成 SQL 语句，无需手写 SQL
- 与 FastAPI 无缝集成

---

## Polars

**[Polars](https://pola.rs/)** 是一个高性能的 DataFrame 库，专为处理大规模数据而设计。与 pandas 相比，Polars 具有以下优势：

- **速度快**：底层用 Rust 编写，利用所有 CPU 核心并行计算
- **内存友好**：支持延迟执行（Lazy API），只在需要时才计算
- **表达式式 API**：链式调用，代码更简洁

```python
# 对比 pandas 的链式操作，Polars 更加直观高效
```

> **注意**：如果你的处理器较旧（不支持 AVX 指令集），请安装 `polars-lts-cpu` 替代：
> ```bash
> pip install polars-lts-cpu
> ```

---

## PyEcharts

**[PyEcharts](https://pyecharts.org/)** 是一个用于生成交互式图表的 Python 库，基于流行的 JavaScript 图表库 ECharts。你可以用纯 Python 代码创建美观、可交互的图表：

- 支持折线图、柱状图、饼图、散点图、地图等 30+ 种图表类型
- 图表支持缩放、悬停提示、数据导出等交互功能
- 可输出为 HTML 文件，直接在浏览器中打开
- 适合在 Jupyter Notebook 中快速可视化数据

---

## Pydantic

**[Pydantic](https://docs.pydantic.dev/)** 是一个基于 Python 类型注解的数据校验库。你只需定义一个继承 `BaseModel` 的类，Pydantic 就会自动完成数据校验、类型转换和错误提示。

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
```

- 利用 Python 3.14 的类型注解进行声明式定义
- 校验失败时提供清晰的错误信息
- 支持 JSON Schema 导出，便于 API 文档生成
- 是 FastAPI、SQLModel 等框架的基石

---

## FastAPI

**[FastAPI](https://fastapi.tiangolo.com/)** 是一个现代化的 Web 框架，用于构建 REST API。它凭借出色的性能和开发体验，已成为 Python Web 开发的主流选择之一：

- **高性能**：与 Node.js、Go 相当
- **自动文档**：自动生成 Swagger UI 和 ReDoc 交互式 API 文档
- **类型安全**：基于 Pydantic + 类型注解，编译期即可发现错误
- **异步支持**：原生支持 `async`/`await`

FastAPI 的核心理念是**利用 Python 类型系统**，这正是你在本书中反复练习的内容。如果你能熟练使用类型注解，FastAPI 上手会非常自然。

---

## asyncio vs trio vs anyio

当程序需要同时处理多个任务（如网络请求、文件读写）时，我们需要**异步编程**。你已经学过的 **生成器（Generator）**（见[迭代器与生成器](./15-iteration.md)）可以暂停和恢复执行——异步编程的核心思想与之非常相似，只是暂停的不是迭代，而是 I/O 操作（如等待网络响应）。

### asyncio

**[asyncio](https://docs.python.org/zh-cn/3.14/library/asyncio.html)** 是 Python 标准库自带的异步框架，从 Python 3.4 起加入，3.7 起通过 `async`/`await` 关键字成为语言特性。

- ✅ 标准库，无需额外安装
- ✅ 生态最广，几乎所有异步库都基于它
- ❌ 取消任务（Cancel）较复杂
- ❌ 错误信息有时不够直观

### Trio

**[Trio](https://trio.readthedocs.io/)** 是一个第三方异步框架，由 Python 核心开发者设计，旨在让异步编程更简单、更安全：

- ✅ 结构化并发：任务有明确的作用域，不会"泄漏"
- ✅ 取消机制更直观、更安全
- ✅ 错误信息更清晰
- ❌ 生态不如 asyncio 丰富
- ❌ 需要额外安装

### AnyIO

**[AnyIO](https://anyio.readthedocs.io/)** 是一个统一的异步后端抽象层，由 Trio 生态的核心开发者 Alex Grönholm 创建。它让你用同一套 API 编写异步代码，并自由选择在 asyncio **或** Trio 上运行。

- ✅ 统一 API，同一份代码可无缝切换 asyncio / Trio 后端
- ✅ 结构化并发（TaskGroup），与 Trio 的 nursery 理念一致
- ✅ 内置 pytest 插件，无需额外安装 pytest-asyncio
- ✅ 内置异步文件 I/O（`open_file`、异步 `Path`）
- ❌ 多一层抽象，增加间接性

### 怎么选？

| 场景                                       | 推荐                  |
| ------------------------------------------ | --------------------- |
| 学习异步概念、编写新项目                   | Trio（更易理解）      |
| 使用主流库（如 FastAPI、aiohttp）          | asyncio（生态优势）   |
| 编写需要同时兼容 asyncio 和 Trio 的库/框架 | AnyIO（统一后端抽象） |
| 两者都了解                                 | 最佳——底层原理相通    |

---

以上就是本书的全部内容。从第一行 `print("Hello, Python")` 走到这里，你已经拥有了扎实的 Python 基础。这些现代化库就是你下一步探索的方向。祝你编程愉快！
