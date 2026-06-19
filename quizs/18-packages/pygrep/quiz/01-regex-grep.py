"""目标：为 pygrep 实现正则表达式匹配功能。

`pygrep` 包（位于 `src/pygrep/`）是一个极简的文本搜索工具。
当前它只支持纯文本匹配。你需要为其添加正则表达式支持。

具体要求：修改 `src/pygrep/core.py`，实现以下两个函数：

- `contains_regex(pattern, text)` —— 使用 `re.search()` 检查文本是否能匹配正则
- `filter_lines_regex(pattern, lines)` —— 返回所有能匹配正则的行

完成后，`pygrep -r` 就可以使用正则表达式搜索了。

本文件通过两种方式测试你的实现：
1. 直接调用 contains_regex / filter_lines_regex
2. 模拟命令行参数调用 `pygrep.__main__.main()`

请确保在 `pygrep/` 目录下运行：
    uv run python quiz/01-regex-grep.py
"""

import io
import sys
from pygrep.core import contains_regex, filter_lines_regex


# ── 单元测试：直接调用 contains_regex ──────────────────────────

def test_basic_digit_pattern() -> bool:
    """基本数字模式匹配。

    >>> test_basic_digit_pattern()
    True
    """
    return contains_regex(r"\d{3}-\d{4}", "电话: 123-4567")


def test_anchor() -> bool:
    """行首 / 行尾锚定。

    >>> test_anchor()
    True
    """
    return (
        contains_regex(r"^Hello", "Hello World")
        and not contains_regex(r"^Hello", "Say Hello")
    )


def test_char_class() -> bool:
    """字符类 —— 全串无元音应返回 False。

    >>> test_char_class()
    True
    """
    return contains_regex(r"[aeiou]", "sky") is False


# ── 单元测试：直接调用 filter_lines_regex ──────────────────────

def test_filter_digits() -> list[str]:
    """过滤包含数字的行。

    >>> test_filter_digits()
    ['123', 'a1b']
    """
    return filter_lines_regex(r"\d+", ["abc", "123", "a1b", "hello"])


# ── 集成测试：模拟命令行调用 ──────────────────────────────────

def run_pygrep(args: list[str], stdin_text: str = "") -> str:
    """模拟命令行运行 `pygrep`，返回标准输出。

    临时替换 sys.argv / sys.stdout / sys.stdin 来模拟调用。
    """
    old_argv = sys.argv
    old_stdout = sys.stdout
    old_stdin = sys.stdin

    sys.argv = ["pygrep", *args]
    sys.stdout = io.StringIO()
    sys.stdin = io.StringIO(stdin_text)

    try:
        from pygrep.__main__ import main

        main()
        return sys.stdout.getvalue()
    finally:
        sys.argv = old_argv
        sys.stdout = old_stdout
        sys.stdin = old_stdin


def test_cli_regex_stdin() -> str:
    """通过标准输入，用 -r 搜索电话号码。

    >>> test_cli_regex_stdin()
    '123-4567\\n'
    """
    data = "联系方式: 123-4567\n地址: 北京市\n"
    return run_pygrep(["-r", r"\d{3}-\d{4}"], data)


def test_cli_regex_no_match() -> str:
    """无匹配时返回空字符串。

    >>> test_cli_regex_no_match()
    ''
    """
    data = "hello\nworld\n"
    return run_pygrep(["-r", r"^\d+$"], data)


def test_cli_plain_text_still_works() -> str:
    """不使用 -r 时，纯文本匹配仍然正常。

    >>> test_cli_plain_text_still_works()
    'hello\\n'
    """
    data = "hello\nworld\n"
    return run_pygrep(["hello"], data)


if __name__ == "__main__":
    import doctest

    results = doctest.testmod(verbose=True)
    if results.failed == 0:
        print("\n🎉 所有测试通过！")
    else:
        print(f"\n❌ {results.failed} 个测试失败，请检查输出。")
