# 目标：输入一个正整数 N，计算从 1 到 N 的和并输出。
# 提示：用 for 循环配合 range() 实现累加。

n = int(input())

total = 0
for i in range(1, n + 1):
    total += i

print(total)
