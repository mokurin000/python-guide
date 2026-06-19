"""目标：掌握 pathlib 模块的基本路径操作。

使用 Path 对象完成路径拼接、属性获取和路径检查等操作。

提示：
- `Path("path")` 创建路径对象
- `/` 运算符拼接路径：`Path("dir") / "file.txt"`
- `Path.joinpath("a", "b")` 拼接多个路径
- `.name`、`.stem`、`.suffix`、`.parent` 获取路径属性
"""

from pathlib import Path


def get_file_info(path: str) -> dict:
    """返回文件路径的各部分信息字典。

    返回字典包含以下键：
    - name: 文件名（含扩展名）
    - stem: 文件名（不含扩展名）
    - suffix: 扩展名
    - parent: 父目录的字符串表示

    >>> info = get_file_info("/home/user/data/file.txt")
    >>> info["name"]
    'file.txt'
    >>> info["stem"]
    'file'
    >>> info["suffix"]
    '.txt'
    >>> info["parent"]
    '/home/user/data'
    >>> get_file_info("archive.tar.gz")["stem"]
    'archive.tar'
    """
    raise NotImplementedError("代码未实现")


def join_paths(base: str, *parts: str) -> str:
    """使用 Path 拼接路径，返回字符串形式。

    提示：可以使用 / 运算符或 joinpath()。

    >>> join_paths("/home/user", "docs", "readme.txt")
    '/home/user/docs/readme.txt'
    >>> join_paths("data", "subdir", "file.json")
    'data/subdir/file.json'
    >>> join_paths("/tmp")
    '/tmp'
    """
    raise NotImplementedError("代码未实现")


def has_extension(path: str, ext: str) -> bool:
    """检查路径是否具有指定的扩展名。

    注意：ext 可能带点（如 '.txt'）也可能不带（如 'txt'）。

    >>> has_extension("data.txt", ".txt")
    True
    >>> has_extension("data.txt", "txt")
    True
    >>> has_extension("data.txt", ".json")
    False
    >>> has_extension("archive.tar.gz", ".gz")
    True
    """
    raise NotImplementedError("代码未实现")


def replace_extension(path: str, new_ext: str) -> str:
    """替换文件路径的扩展名。

    如果 new_ext 不以点开头，则自动添加点。

    >>> replace_extension("data.txt", ".json")
    'data.json'
    >>> replace_extension("data.txt", "csv")
    'data.csv'
    >>> replace_extension("archive.tar.gz", ".zip")
    'archive.tar.zip'
    >>> replace_extension("file", ".txt")
    'file.txt'
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
