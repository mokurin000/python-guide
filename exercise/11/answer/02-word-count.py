# 目标：输入多行文本（以空行结束），统计每个单词出现的次数。
# 输入格式：若干行英文单词，每行一个单词，以空行结束。
# 输出格式：每行输出 "单词: 次数"，按单词出现顺序输出。
# 提示：用 for 循环遍历输入，字典存储计数。

word_counts = {}

word = input()
while word != "":
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
    word = input()

for word, count in word_counts.items():
    print(f"{word}: {count}")
