# 源码

本书基于 `mdbook` 实现，在添加章节时应当添加到 `src/SUMMARY.md` 最后。

# 代码运行

总是使用 `bash -c '...'` 而非 PowerShell 进行操作。

`rg`, `python3` 已安装并提供在`PATH`中。

# Roadmap

Roadmap 位于 `README.md` 内。

你不得对其内容进行任何修改，只得将完成的部分进行打勾。

# 练习文件约定

## 文件结构

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

## 命名规则

- 练习文件名使用连字符 `-` 而非下划线，例如 `01-max-in-list.py`。
- 输入/输出文件扩展名为 `.in1`, `.in2` / `.out1`, `.out2`。

## 学生存根要求

每个练习文件需要包含：
1. 题目背景（中文注释）
2. 相关特性的提示（中文注释）
3. `raise NotImplementedError("代码未实现")` 占位符，用于跳过未完成的练习
4. 用 `...` 作为代码中需要替换部分的占位提示
5. 参考实现位于 `answer/`，保持注释部分一致

## 术语

中文术语后用括号标注英文术语，例如：列表 (list)、字典 (dict)、集合 (set)。

hashable: 可计算哈希

# run_tests.py

这是一个基于 输入/输出 的测试脚本，用于提供 `函数` 章节之前的代码测试。

在 `函数` 章节和之后，代码测试将于 `quizs/` 提供，调用 Python 本身的 `doctest` 原地进行测试。
