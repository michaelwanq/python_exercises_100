"""
编写函数，传入.txt文件路径作为参数，统计文件中英文单词的数目
注意，不只是空格分割，也可能是逗号分隔
"""
import re

def count_words(filepath):
    with open(filepath) as file:
        string = file.read()
        string_list = re.split(r",| ", string)
        print(string_list)
        return len(string_list)

print(count_words("count.txt"))