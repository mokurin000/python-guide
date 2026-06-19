"""目标：使用 open() 读取真实的文本文件和二进制文件。

给定位于 `text/sample.txt` 和 `binary/sample.bin` 的两个文件，
请使用 `open()` 和 `with` 语句读取它们，返回文件的内容。

提示：
- 使用 `with open(path, encoding="utf-8") as f:` 读取文本文件
- 使用 `with open(path, "rb") as f:` 读取二进制文件
- 使用 `__file__` 获取当前脚本所在目录，再拼接到 `text/` 和 `binary/`
- f.read() 读取全部内容；逐行读取用 `for line in f:` 或 `f.readlines()`
"""

from pathlib import Path

# 文件路径：基于当前脚本的位置
HERE = Path(__file__).parent
TEXT_FILE = HERE / "text" / "sample.txt"
BINARY_FILE = HERE / "binary" / "sample.bin"


def read_text(filepath: str | Path = TEXT_FILE) -> str:
    """以文本模式读取文件，返回全部内容字符串。

    >>> result = read_text()
    >>> result[:20]
    'Hello, 文件读写!\\nPyt'
    """
    raise NotImplementedError("代码未实现")


def read_binary(filepath: str | Path = BINARY_FILE) -> bytes:
    """以二进制模式读取文件，返回全部字节内容。

    >>> data = read_binary()
    >>> len(data)
    1024
    >>> data[:4]
    b'\\x00\\x01\\x02\\x03'
    >>> data[-4:]
    b'\\xfc\\xfd\\xfe\\xff'
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
    import hashlib
    import doctest

    print("=" * 50)
    print("doctest 测试结果：")
    print("=" * 50)
    doctest.testmod(verbose=True)

    # === 哈希验证：检查读取内容的完整性 ===
    # 以下代码用 hashlib 对读取结果做哈希，确保你确实读到了正确的文件内容。
    # 你无法通过直接返回固定字符串来"作弊"——程序会验证实际读到的数据。
    print()
    print("=" * 50)
    print("哈希验证结果：")
    print("=" * 50)

    all_pass = True

    # 验证文本文件
    try:
        text_content = read_text()
        text_hash = hashlib.sha256(text_content.encode("utf-8")).hexdigest()
        expected_text_hash = (
            "186cd6a1da768549f9bb6999342785dcec409465a4f94a84cb941475517845ca"
        )
        if text_hash == expected_text_hash:
            print("[PASS] read_text() 读取内容正确")
        else:
            print(f"[FAIL] read_text() 哈希不匹配")
            print(f"       期望: {expected_text_hash}")
            print(f"       实际: {text_hash}")
            all_pass = False
    except NotImplementedError:
        print("[SKIP] read_text() 尚未实现")
        all_pass = False

    # 验证二进制文件
    try:
        binary_data = read_binary()
        binary_hash = hashlib.sha256(binary_data).hexdigest()
        expected_binary_hash = (
            "785b0751fc2c53dc14a4ce3d800e69ef9ce1009eb327ccf458afe09c242c26c9"
        )
        if binary_hash == expected_binary_hash:
            print("[PASS] read_binary() 读取内容正确")
        else:
            print(f"[FAIL] read_binary() 哈希不匹配")
            print(f"       期望: {expected_binary_hash}")
            print(f"       实际: {binary_hash}")
            all_pass = False
    except NotImplementedError:
        print("[SKIP] read_binary() 尚未实现")
        all_pass = False

    print()
    if all_pass:
        print("🎉 所有哈希验证通过！")
    else:
        print("部分哈希验证未通过，请按提示修改代码。")
