# 目标：输入 N 个整数，输出其中所有偶数的平方组成的列表。
# 输入格式：
#   第一行：N（整数的个数）
#   接下来 N 行：每行一个整数
# 输出格式：一行，输出列表
# 提示：用列表推导式 + if 条件过滤。

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

result = [x**2 for x in nums if x % 2 == 0]

print(result)
