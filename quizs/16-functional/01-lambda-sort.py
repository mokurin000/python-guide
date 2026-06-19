"""目标：用 lambda 作为排序 key。

给定一个包含学生信息的列表，每个元素为 (姓名, 年龄, 成绩) 的三元组。
请你实现以下函数，使用 `lambda` 作为 `sorted()` 的 `key` 参数来完成排序。

提示：`sorted(iterable, key=func)` 中的 `key` 参数指定一个函数，
该函数作用于每个元素上，返回的值作为排序依据。
"""


def sort_by_age(students: list[tuple[str, int, float]]) -> list[tuple[str, int, float]]:
    """按年龄升序排序。

    >>> students = [("Alice", 22, 88.5), ("Bob", 19, 92.0), ("Charlie", 21, 75.5)]
    >>> sort_by_age(students)
    [('Bob', 19, 92.0), ('Charlie', 21, 75.5), ('Alice', 22, 88.5)]
    """
    raise NotImplementedError("代码未实现")


def sort_by_score_desc(
    students: list[tuple[str, int, float]],
) -> list[tuple[str, int, float]]:
    """按成绩降序排序。

    >>> students = [("Alice", 22, 88.5), ("Bob", 19, 92.0), ("Charlie", 21, 75.5)]
    >>> sort_by_score_desc(students)
    [('Bob', 19, 92.0), ('Alice', 22, 88.5), ('Charlie', 21, 75.5)]
    """
    raise NotImplementedError("代码未实现")


def sort_by_name_length(names: list[str]) -> list[str]:
    """按名字长度升序排序；长度相同时保持原顺序。

    >>> sort_by_name_length(["banana", "apple", "cherry", "date"])
    ['date', 'apple', 'banana', 'cherry']
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
