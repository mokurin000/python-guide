"""目标：综合运用 lambda、map、filter、reduce 和 partial。

实现一个简单的数据处理管道函数 `analyze_scores`，
它接收一个学生成绩列表，完成以下步骤：

1. 过滤出成绩 >= 60 的学生（及格）
2. 提取他们的成绩（使用 map）
3. 计算平均分（使用 reduce）
4. 最后用 lambda 配合 sorted 返回按成绩升序排列的及格学生列表

另外还有两个使用 partial 的辅助函数。

提示：将每一步的结果用变量保存，使代码清晰可读。
"""

from functools import reduce, partial


def analyze_scores(
    students: list[tuple[str, int]],
) -> tuple[float, list[tuple[str, int]]]:
    """分析学生成绩，返回 (平均分, 按成绩升序的及格学生列表)。

    >>> scores = [("Alice", 85), ("Bob", 42), ("Charlie", 73), ("David", 90)]
    >>> avg, passed = analyze_scores(scores)
    >>> round(avg, 2)
    82.67
    >>> passed
    [('Charlie', 73), ('Alice', 85), ('David', 90)]
    """
    raise NotImplementedError("代码未实现")


def create_grade_boundary(pass_score: int):
    """使用 partial 创建及格线判断函数。
    原函数为 `def is_passing(score, pass_score): ...`，
    用 partial 固定 pass_score 参数。

    >>> is_pass = create_grade_boundary(60)
    >>> is_pass(85)
    True
    >>> is_pass(42)
    False
    >>> is_pass(60)
    True
    """
    raise NotImplementedError("代码未实现")


def create_score_extractor():
    """返回一个使用 map 提取成绩的偏函数。
    原函数为 `def extract_scores(students, func): ...`，
    你需要用 map 和 partial 配合，创建一个专门提取学生成绩的函数。

    >>> extract = create_score_extractor()
    >>> students = [("Alice", 85), ("Bob", 42), ("Charlie", 73)]
    >>> extract(students)
    [85, 42, 73]
    >>> extract([])
    []
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
