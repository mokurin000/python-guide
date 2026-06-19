"""目标：使用 open() 和 with 语句写入真实的文件。

实现以下函数，将数据写入指定的文件路径。写入后，`if __name__ == "__main__"`
中的测试代码会用 `hashlib` 读取文件并验证哈希——你无法通过返回固定字符串作弊。

提示：
- 使用 `with open(filepath, "w", encoding="utf-8") as f:` 写入文本
- 使用 `with open(filepath, "wb") as f:` 写入二进制数据
- `f.write(content)` 写入字符串或字节
- `f.writelines(lines)` 写入多行
"""

from pathlib import Path


def write_text(content: str, filepath: str | Path) -> None:
    """将 content 以文本模式写入 filepath。

    >>> import tempfile, os
    >>> tmp = tempfile.mkstemp(suffix='.txt')[1]
    >>> write_text("Hello\\nWorld\\n", tmp)
    >>> open(tmp).read()
    'Hello\\nWorld\\n'
    >>> os.unlink(tmp)

    >>> tmp2 = tempfile.mkstemp(suffix='.txt')[1]
    >>> write_text("Python 文件读写\\n", tmp2)
    >>> open(tmp2, encoding="utf-8").read()
    'Python 文件读写\\n'
    >>> os.unlink(tmp2)
    """
    raise NotImplementedError("代码未实现")


def write_binary(data: bytes, filepath: str | Path) -> None:
    """将 data 以二进制模式写入 filepath。

    >>> import tempfile, os
    >>> tmp = tempfile.mkstemp(suffix='.bin')[1]
    >>> write_binary(b'\\x00\\x01\\x02\\x03', tmp)
    >>> open(tmp, 'rb').read()
    b'\\x00\\x01\\x02\\x03'
    >>> os.unlink(tmp)

    >>> tmp2 = tempfile.mkstemp(suffix='.bin')[1]
    >>> data = bytes(range(64))
    >>> write_binary(data, tmp2)
    >>> open(tmp2, 'rb').read() == data
    True
    >>> os.unlink(tmp2)
    """
    raise NotImplementedError("代码未实现")


def write_csv(headers: list[str], rows: list[list[str]], filepath: str | Path) -> None:
    """将 CSV 格式数据写入 filepath。

    第一行为表头，后续每行为数据行，用逗号分隔各列，每行末尾有换行符。

    >>> import tempfile, os
    >>> tmp = tempfile.mkstemp(suffix='.csv')[1]
    >>> h = ["name", "age", "score"]
    >>> r = [["Alice", "20", "95"], ["Bob", "22", "87"]]
    >>> write_csv(h, r, tmp)
    >>> open(tmp).read()
    'name,age,score\\nAlice,20,95\\nBob,22,87\\n'
    >>> os.unlink(tmp)
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import hashlib
    import tempfile
    import os
    import doctest

    print("=" * 50)
    print("doctest 测试结果：")
    print("=" * 50)
    doctest.testmod(verbose=True)

    # === 哈希验证：检查写入内容的完整性 ===
    # 以下代码调用你的写入函数，然后读取文件并计算 sha256 哈希。
    # 如果你没有正确写入数据，或者"伪造"返回值，都能被检测出来。
    print()
    print("=" * 50)
    print("哈希验证结果：")
    print("=" * 50)

    all_pass = True

    def _verify_write(label, write_fn, write_args, tmp_ext, expected_hash):
        """辅助函数：写入文件 → 读取 → 验证哈希。"""
        fd, tmp = tempfile.mkstemp(suffix=tmp_ext)
        os.close(fd)  # 立即关闭 fd，否则 Windows 会锁定文件
        try:
            write_fn(*write_args, tmp)
            with open(tmp, "rb") as f:
                data = f.read()
            h = hashlib.sha256(data).hexdigest()
            if h == expected_hash:
                print(f"[PASS] {label} 写入内容正确")
                return True
            else:
                print(f"[FAIL] {label} 哈希不匹配")
                print(f"       期望: {expected_hash}")
                print(f"       实际: {h}")
                return False
        except NotImplementedError:
            print(f"[SKIP] {label} 尚未实现")
            return False
        except Exception as e:
            print(f"[ERROR] {label}: {e}")
            return False
        finally:
            try:
                os.unlink(tmp)
            except (FileNotFoundError, PermissionError):
                pass

    if not _verify_write(
        "write_text()",
        write_text,
        ("Hello\nWorld\n",),
        ".txt",
        "cc37937f1366919e300be784838d0f648684e2934fde66cd97e333ae51239761",
    ):
        all_pass = False

    if not _verify_write(
        "write_binary()",
        write_binary,
        (bytes(range(64)),),
        ".bin",
        "fdeab9acf3710362bd2658cdc9a29e8f9c757fcf9811603a8c447cd1d9151108",
    ):
        all_pass = False

    if not _verify_write(
        "write_csv()",
        write_csv,
        (["name", "age", "score"], [["Alice", "20", "95"], ["Bob", "22", "87"]]),
        ".csv",
        "8815715425c57faedcd9f53a8d20bf37d6b8b1eb04dd674428589e992a1c12b6",
    ):
        all_pass = False

    print()
    if all_pass:
        print("🎉 所有哈希验证通过！")
    else:
        print("部分哈希验证未通过，请按提示修改代码。")
