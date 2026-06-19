# 目标：输入 N ，再输入 N 个整数，输出这些整数中的最大值。
# 提示：先用 while 循环把数字添加到列表中，再用另一个 while 循环遍历列表找出最大值。

n = int(input())
nums = []

# 在这里将数字逐个添加到 nums 中
i = 0
while i < n:
    nums.append(int(input()))
    i += 1

i = 0
max_num = nums[0]
while i < len(nums):
    if nums[i] > max_num:
        max_num = nums[i]
    i += 1

print(max_num)
