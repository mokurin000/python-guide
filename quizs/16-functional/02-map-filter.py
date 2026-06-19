"""目标：使用 map() 和 filter() 处理数据。

实现以下函数，分别运用 map() 和 filter() 对数据进行变换和筛选。

提示：
- `map(func, iterable)` 对每个元素应用 func，返回迭代器
- `filter(pred, iterable)` 保留 pred 返回 True 的元素
- 返回结果请用 list() 转换为列表
"""


def square_even(numbers: list[int]) -> list[int]:
    """先过滤出偶数，再求每个偶数的平方。

    >>> square_even([1, 2, 3, 4, 5, 6])
    [4, 16, 36]
    >>> square_even([7, 9, 11])
    []
    """
    raise NotImplementedError("代码未实现")


def filter_long_words(words: list[str], min_length: int) -> list[str]:
    """过滤出长度 >= min_length 的单词。

    >>> filter_long_words(["hi", "hello", "world", "a", "python"], 4)
    ['hello', 'world', 'python']
    >>> filter_long_words(["a", "an", "the"], 5)
    []
    """
    raise NotImplementedError("代码未实现")


def name_to_age_greeting(names: list[str]) -> list[str]:
    """将名字列表转换为问候语列表，格式为 "Hello, 名字!"。

    >>> name_to_age_greeting(["Alice", "Bob", "Charlie"])
    ['Hello, Alice!', 'Hello, Bob!', 'Hello, Charlie!']
    >>> name_to_age_greeting([])
    []
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
