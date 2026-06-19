# 目标：输入两个集合，输出它们交集的大小（即共同元素的数量）。
# 输入格式：
#   第一行：N（集合 A 的元素数量）
#   接下来 N 行：集合 A 的元素
#   接下来一行：M（集合 B 的元素数量）
#   接下来 M 行：集合 B 的元素
# 输出：交集的大小（一个整数）
# 提示：先创建两个集合，然后用 & 运算符计算交集，再用 len() 获取大小。

n = int(input())
set_a = set()
i = 0
while i < n:
    set_a.add(int(input()))
    i += 1

m = int(input())
set_b = set()
i = 0
while i < m:
    set_b.add(int(input()))
    i += 1

# 计算交集并输出大小
print(len(set_a & set_b))
