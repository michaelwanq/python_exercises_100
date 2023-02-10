"""
编写代码，生成一个文件p051.txt，每一行是一个英文字母，从a~z
"""
import string
with open('p051.txt', 'w') as file:
    for i in string.ascii_lowercase:
        file.write(i + "\n")
