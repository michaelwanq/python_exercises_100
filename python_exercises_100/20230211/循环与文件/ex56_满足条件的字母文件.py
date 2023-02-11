"""
编写代码，
1、扫描p054文件夹，里面是a.txt/b.txt~z.txt共26个文件，每个文件的都是对应字母a~z
2、如果文件里的内容字母，属于字符串"python"中的字母，则存入结果列表
3、打印结果列表
"""
# import glob
# letters = []
# file_list = glob.glob("p054/*.txt")
# for file in file_list:
#     with open(file) as f:
#         letter = f.read().strip()
#         if letter in 'python':
#             letters.append(letter)
#         else:
#             continue
# print(letters)

import glob

letters = []
file_list = glob.glob("p054/*.txt")
check = "python"

for file in file_list:
  with open(file) as f:
    letter = f.read().strip()
    if letter in check:
        letters.append(letter)

print(letters)

