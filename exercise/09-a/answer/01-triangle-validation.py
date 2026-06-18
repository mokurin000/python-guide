# 输入三条边长，验证它们是否可以构成三角形。
a = int(input())
b = int(input())
c = int(input())

# 如果可以构成，则输出: o
# 如果无法构成，则输出: x

# 此处 `...` 表示代码中被省略掉的部分，你应该把它换成真正的逻辑部分。
# 提示: 三角形成立条件：任意两边长之和大于第三边长。
if a + b > c and a + c > b and b + c > a:
    triangle_validation = "o"
else:
    triangle_validation = "x"

print(triangle_validation)
