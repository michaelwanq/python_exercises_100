"""
编写代码，
1、扫描p054文件夹，里面是a.txt/b.txt~z.txt共26个文件，每个文件的都是对应字母a~z
2、读取每个文件的内容，最终产出一个list，是字母a~z
"""
import glob

letters = []
file_list = glob.glob("p054/*.txt")
print(file_list)

for file in file_list:
    with open(file) as f:
        letters.append(f.read().strip())

print(letters)
