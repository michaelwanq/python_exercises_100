"""
完成如下程序，让用户可以输入一个英文单词，程序给出中文翻译结果
d = {"apple": "苹果", "orange": "桔子", "banana": "香蕉"}
实现效果：
Enter word: apple
苹果
"""
def my_dict(word):
    d = {"apple": "苹果",
         "orange": "桔子",
         "banana": "香蕉"
         }
    while True:
        # word = input('Enter word: ')
        if word != 'quit':
            if word in d.keys():
                print(d[word])
                break
            else:
                print(f'你输入的{word}查询不对，请重新输入！')
                continue
        else:
            break
    print('欢迎再次查询，再见！')

my_dict('apple')

