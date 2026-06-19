import re


def contains(pattern: str, text: str) -> bool:
    """检查 text 中是否包含 pattern（纯文本匹配）。"""
    return pattern in text


def filter_lines(pattern: str, lines: list[str]) -> list[str]:
    """返回包含 pattern 的所有行（纯文本匹配）。"""
    return [line for line in lines if contains(pattern, line)]


def contains_regex(pattern: str, text: str) -> bool:
    """检查 text 中是否能匹配正则表达式 pattern。

    使用 re.search() 实现。

    >>> contains_regex(r"\\d{3}-\\d{4}", "电话: 123-4567")
    True
    >>> contains_regex(r"^Hello", "Hello World")
    True
    >>> contains_regex(r"^Hello", "Say Hello")
    False
    """
    raise NotImplementedError("代码未实现")


def filter_lines_regex(pattern: str, lines: list[str]) -> list[str]:
    """返回能匹配正则表达式 pattern 的所有行。

    >>> filter_lines_regex(r"\\d+", ["abc", "123", "a1b", "hello"])
    ['123', 'a1b']
    """
    raise NotImplementedError("代码未实现")
