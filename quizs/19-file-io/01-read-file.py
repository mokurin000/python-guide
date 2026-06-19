"""目标：使用 open() 读取真实的文本文件和二进制文件，并用 hashlib 验证内容。

给定位于 `text/sample.txt` 和 `binary/sample.bin` 的两个文件，
请使用 `open()` 和 `with` 语句读取它们，并用 `hashlib.sha256()` 验证内容。

提示：
- 使用 `with open(path, encoding="utf-8") as f:` 读取文本文件
- 使用 `with open(path, "rb") as f:` 读取二进制文件
- `hashlib.sha256(data).hexdigest()` 返回 64 字符的十六进制哈希值
- 使用 `__file__` 获取当前脚本所在目录，再拼接到 `text/` 和 `binary/`
"""

import hashlib
from pathlib import Path

# 文件路径：基于当前脚本的位置
HERE = Path(__file__).parent
TEXT_FILE = HERE / "text" / "sample.txt"
BINARY_FILE = HERE / "binary" / "sample.bin"


def read_text_and_hash(filepath: str | Path = TEXT_FILE) -> str:
    """以文本模式读取文件，返回其内容的 sha256 十六进制字符串。

    >>> read_text_and_hash()
    '186cd6a1da768549f9bb6999342785dcec409465a4f94a84cb941475517845ca'
    """
    raise NotImplementedError("代码未实现")


def read_binary_and_hash(filepath: str | Path = BINARY_FILE) -> str:
    """以二进制模式读取文件，返回其内容的 sha256 十六进制字符串。

    >>> read_binary_and_hash()
    '785b0751fc2c53dc14a4ce3d800e69ef9ce1009eb327ccf458afe09c242c26c9'
    """
    raise NotImplementedError("代码未实现")


def count_lines_in_text(filepath: str | Path = TEXT_FILE) -> int:
    """统计文本文件的行数（包括空行）。

    >>> count_lines_in_text()
    7
    """
    raise NotImplementedError("代码未实现")


def filter_lines_in_text(keyword: str, filepath: str | Path = TEXT_FILE) -> list[str]:
    """读取文本文件，返回包含指定关键字的行（不含换行符）。

    >>> filter_lines_in_text("Python")
    ['Python 的 open() 函数可以打开文件。']
    >>> filter_lines_in_text("文件")
    ['Hello, 文件读写!', 'Python 的 open() 函数可以打开文件。', '使用 encoding="utf-8" 来处理中文。']
    >>> filter_lines_in_text("不存在的内容")
    []
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
