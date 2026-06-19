"""目标：使用 open() 和 with 语句写入真实的文件，并用 hashlib 验证写入内容。

实现以下函数，将数据写入指定的文件路径，然后计算文件的 sha256 哈希，
确保写入的内容与预期一致。

提示：
- 使用 `with open(filepath, "w", encoding="utf-8") as f:` 写入文本
- 使用 `with open(filepath, "wb") as f:` 写入二进制数据
- `hashlib.sha256(data).hexdigest()` 计算哈希
- 先用 `f.write()` 写入内容，再打开文件读取并计算哈希
"""

import hashlib
from pathlib import Path


def write_text_and_hash(content: str, filepath: str | Path) -> str:
    """将 content 以文本模式写入 filepath，返回写入内容的 sha256 哈希。

    写入完成后，重新以二进制模式打开文件，计算 sha256 返回。

    >>> import tempfile, os
    >>> tmp = tempfile.mkstemp(suffix='.txt')[1]
    >>> write_text_and_hash("Hello\\nWorld\\n", tmp)
    'cc37937f1366919e300be784838d0f648684e2934fde66cd97e333ae51239761'
    >>> os.unlink(tmp)

    >>> tmp2 = tempfile.mkstemp(suffix='.txt')[1]
    >>> write_text_and_hash("Python 文件读写\\n", tmp2)
    'ca4617e2e636fb83ed3b067e6b5c0dbc8b59b6c2a29ed0f01f5874e04786dc4c'
    >>> os.unlink(tmp2)
    """
    raise NotImplementedError("代码未实现")


def write_binary_and_hash(data: bytes, filepath: str | Path) -> str:
    """将 data 以二进制模式写入 filepath，返回写入数据的 sha256 哈希。

    >>> import tempfile, os
    >>> tmp = tempfile.mkstemp(suffix='.bin')[1]
    >>> write_binary_and_hash(b'\\x00\\x01\\x02\\x03', tmp)
    '054edec1d0211f624fed0cbca9d4f9400b0e491c43742af2c5b0abebf0c990d8'
    >>> os.unlink(tmp)

    >>> tmp2 = tempfile.mkstemp(suffix='.bin')[1]
    >>> data = bytes(range(64))
    >>> write_binary_and_hash(data, tmp2)
    'fdeab9acf3710362bd2658cdc9a29e8f9c757fcf9811603a8c447cd1d9151108'
    >>> os.unlink(tmp2)
    """
    raise NotImplementedError("代码未实现")


def write_csv_and_hash(
    headers: list[str], rows: list[list[str]], filepath: str | Path
) -> str:
    """将 CSV 格式数据写入 filepath，返回文件的 sha256 哈希。

    第一行为表头，后续每行为数据行，用逗号分隔各列，每行末尾有换行符。

    >>> import tempfile, os
    >>> tmp = tempfile.mkstemp(suffix='.csv')[1]
    >>> h = ["name", "age", "score"]
    >>> r = [["Alice", "20", "95"], ["Bob", "22", "87"]]
    >>> write_csv_and_hash(h, r, tmp)
    '8815715425c57faedcd9f53a8d20bf37d6b8b1eb04dd674428589e992a1c12b6'
    >>> os.unlink(tmp)
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
