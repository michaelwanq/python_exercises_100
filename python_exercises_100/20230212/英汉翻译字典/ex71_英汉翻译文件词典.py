"""
如下是英汉翻译词典文件，用python加载词典文件
当用户输入英语单词时，返回中文文字
增加：程序应该处理大小写情况，例如输入Apple也能返回apple的翻译
自己新建 p071.txt 粘贴如下内容过去
效果
Enter word: Apple
苹果
"""
engdict = {}
with open("p071.txt", encoding="utf8") as f:
    for line in f:
        eng, ch = line.strip().split(",")
        engdict[eng] = ch


def translate(word):
    try:
        return engdict[word]
    except KeyError:
        return "单词不在词典中"


word = input("Enter word: ").lower()
print(translate(word))
