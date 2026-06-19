"""目标：理解 `with` 语句和文件对象的上下文管理。

实现以下函数，使用 `with` 语句进行文件操作。
由于 doctest 使用模拟数据，这里我们模拟文件的打开和读取行为。

提示：
- `with open(...) as f:` 会在代码块结束后自动关闭文件
- 文件对象是可迭代的：`for line in f:`
- `f.read()` 读取全部内容
- 使用 `io.StringIO` 可以模拟文件对象
"""

from io import StringIO


def read_file_simulated(content: str) -> list[str]:
    """模拟 `with open() as f: for line in f:` 的行为。

    将 content 视为文件内容，逐行读取，返回不含换行符的行列表。

    >>> read_file_simulated("Hello\\nWorld\\n")
    ['Hello', 'World']
    >>> read_file_simulated("a\\nb\\nc\\n")
    ['a', 'b', 'c']
    >>> read_file_simulated("")
    []
    """
    # 使用 StringIO 模拟文件对象，不要修改此代码
    f = StringIO(content)
    result = []
    # 在此之下使用 `with` 风格的逐行读取
    # ...existing code...
    raise NotImplementedError("代码未实现")


def safe_read_lines(lines: list[str]) -> list[str]:
    """使用 with 语句的思维：先打开（模拟），再读取，然后自动"关闭"。

    本题模拟一个"资源管理器"，请将 lines 中的每一行用 strip() 处理后返回。

    >>> safe_read_lines(["  hello  \\n", "  world  \\n"])
    ['hello', 'world']
    >>> safe_read_lines(["  Python  \\n", "  is  \\n", "  fun  \\n"])
    ['Python', 'is', 'fun']
    >>> safe_read_lines([])
    []
    """
    raise NotImplementedError("代码未实现")


def write_and_read_simulated(data: list[str]) -> str:
    """模拟先写入再读取的过程。

    将 data 中的每个元素作为一行（末尾加换行符）写入 StringIO，
    然后读取全部内容返回。

    >>> write_and_read_simulated(["apple", "banana"])
    'apple\\nbanana\\n'
    >>> write_and_read_simulated(["single"])
    'single\\n'
    >>> write_and_read_simulated([])
    ''
    """
    # 使用 StringIO 模拟文件对象
    f = StringIO()
    # ...existing code...
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
