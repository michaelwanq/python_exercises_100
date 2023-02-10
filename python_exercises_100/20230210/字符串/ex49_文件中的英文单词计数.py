"""
文件中的英文单词计数
编写函数，传入.txt文件路径作为参数，统计文件中英文单词的数目
"""
def count_words(filepath):
    with open(filepath) as file:
        string = file.read()
    string_list = string.split()
    return len(string_list)

print(count_words("count.txt"))