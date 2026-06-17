"""
示例程序: 调用 input(提示词) 以读取输入的文本
"""

import sys

# Python input() 会把提示词发送到程序输出的同一通道
print("What's your name? ", flush=True, file=sys.stderr)
name: str = input()
print(f"Hello, {name.capitalize()}!")

print("Type an integer: ", flush=True, file=sys.stderr)
# 给 int() 传入 input() 返回的字符串，把它转换成整数类型。
num: int = int(input())
print(f"2**{num} is {2**num}")
