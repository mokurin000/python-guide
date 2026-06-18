# 输入体重 (kg)
weight = float(input())
# 输入身高 (cm)
height = int(input()) / 100

# 目标：输出保留两位小数的计算结果
bmi = round(weight / height**2, 2)
print(bmi)
