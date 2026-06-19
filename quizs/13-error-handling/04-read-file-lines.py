"""目标：实现 read_file_lines(filename)，尝试打开文件并返回行列表（去除末尾换行符）。
如果文件不存在，返回空列表 []。

提示：使用 try...except 捕获 FileNotFoundError。
在 except 块中 return []。
在 try 块中使用 with open(filename, "r") as f: 和 f.readlines() 读取所有行。
使用列表推导式或 strip() 去除每行末尾的换行符。
"""


def read_file_lines(filename):
    """读取文件内容，返回去除换行符后的行列表。

    # 测试文件存在的情况（需要先创建测试文件）
    # 测试文件不存在的情况
    >>> read_file_lines("nonexistent_file_xyz.txt")
    []
    """
    raise NotImplementedError("代码未实现")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
