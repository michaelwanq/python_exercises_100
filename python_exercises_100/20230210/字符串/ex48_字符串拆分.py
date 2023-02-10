"""
创建一个函数，以任何一个英文字符串作为入参，返回英文单词的数目

"""


def count_words(string):
    string_list = string.split()
    return len(string_list)


print(count_words("i am a good boy"))
