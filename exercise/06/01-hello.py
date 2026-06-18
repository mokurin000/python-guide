"""
示例程序: 调用 input() 以读取输入的文本
"""

name: str = input()
print(f"Hello, {name.capitalize()}!")

# 给 int() 传入 input() 返回的字符串，把它转换成整数类型。
num: int = int(input())
print(f"2**{num} is {2**num}")
