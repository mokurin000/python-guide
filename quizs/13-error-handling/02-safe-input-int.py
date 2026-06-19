"""目标：实现 safe_input_int(prompt)，不断提示用户输入，直到输入一个有效的整数。
每次输入无效时打印提示信息 "输入无效，请重新输入"。

提示：使用 while True 循环，在 try 块中尝试 int(input(prompt))，
如果成功则 return，如果捕获到 ValueError 则继续循环。
"""


def safe_input_int(prompt: str) -> int:
    """循环直到用户输入一个有效的整数。

    >>> safe_input_int("输入：")  # 测试时手动输入 "abc" 然后 "42"
    42
    >>> safe_input_int("> ")     # 测试时手动输入 "3.14" 然后 "-5"
    -5
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
