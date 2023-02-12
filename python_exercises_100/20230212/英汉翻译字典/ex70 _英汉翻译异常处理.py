"""
如下程序实现功能，让用户可以输入一个英文单词，程序给出中文翻译结果
修改程序，如果输入的英文单词不在字典中，输出信息“单词不在词典中”
d = {"apple": "苹果", "orange": "桔子", "banana": "香蕉"}

def translate(word):
    return d[word]

word = input("Enter word: ")
print(translate(word))
限制：请使用try catch的异常机制完成本题目，效果如下
Enter word: hello
单词不在词典中
"""
d = {"apple": "苹果", "orange": "桔子", "banana": "香蕉"}

d = {"apple": "苹果", "orange": "桔子", "banana": "香蕉"}

def translate(word):
    try:
        return d[word]
    except KeyError:
        return "单词不在词典中"

word = input("Enter word: ")
print(translate(word))
