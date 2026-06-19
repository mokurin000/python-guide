# 源码

本书基于 `mdbook` 实现，在添加章节时应当添加到 `src/SUMMARY.md` 最后。

# 代码运行

总是使用 `bash -c '...'` 而非 PowerShell 进行操作。

`rg`, `python3` 已安装并提供在`PATH`中。

# Roadmap

Roadmap 位于 `README.md` 内。

你不得对其内容进行任何修改，只得将完成的部分进行打勾。

# 练习文件约定

## Day 1-4：exercise/ + run_tests.py (基于 I/O)

文件结构：

```
exercise/<章节>/
├── 01-exercise-name.py     # 学生编辑的练习文件
├── answer/
│   └── 01-exercise-name.py # 参考实现
├── in/
│   ├── 01-exercise-name.in1 # 测试输入（按编号）
│   └── 01-exercise-name.in2
└── out/
    ├── 01-exercise-name.out1 # 预期输出（与 .in 编号对应）
    └── 01-exercise-name.out2
```

测试由 `run_tests.py` 驱动，比较程序的标准输出与 `.out` 文件。

## Day 5+：quizs/ + doctest (自包含测试)

从 Day 5 开始，不再使用 `exercise/` 和 `run_tests.py`。练习文件直接放在 `quizs/<章节>/` 下，每个文件自包含 `doctest` 测试用例。学生手动运行 `python quizs/<章节>/<文件>.py` 来验证。

文件结构：

```
quizs/
├── <章节>/
│   ├── 01-exercise-name.py     # 练习文件（含 doctest）
│   ├── 02-exercise-name.py
│   └── ...
```

练习文件格式：

```python
"""目标：<题目描述>

提示：<相关特性的提示>
"""

def func(...):
    """<函数说明>

    >>> func(输入)
    预期输出
    >>> func(输入)
    预期输出
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
```

## 命名规则

- 练习文件名使用连字符 `-` 而非下划线，例如 `01-max-in-list.py`。

## 学生存根要求

每个练习文件需要包含：
1. 题目背景（中文注释或文档字符串）
2. 相关特性的提示
3. `raise NotImplementedError("代码未实现")` 占位符
4. 用 `...` 作为代码中需要替换部分的占位提示

## 术语

中文术语后用括号标注英文术语，例如：列表 (list)、字典 (dict)、集合 (set)。

hashable: 可计算哈希
