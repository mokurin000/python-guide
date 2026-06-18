# 输入一个考试成绩，输入保证不大于100、不小于0。
score = int(input())

# 根据成绩输出等级：
# [90, 100] -> A
# [80, 90)  -> B
# [70, 80)  -> C
# [60, 70)  -> D
# [0, 60)   -> F

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(grade)
