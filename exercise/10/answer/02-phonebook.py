# 目标：模拟电话簿查询功能。
# 先输入若干行姓名和电话号码（交替输入），以 "--" 结束；
# 然后输入一个要查询的姓名，输出对应的电话号码。
# 如果姓名不存在，输出 "Not found"。

phonebook = {}

# 交替读取姓名和号码，直到遇到 "--"
name = input()
while name != "--":
    phone = input()
    phonebook[name] = phone
    name = input()

# 读取要查询的姓名并输出结果
query = input()
if query in phonebook:
    print(phonebook[query])
else:
    print("Not found")
