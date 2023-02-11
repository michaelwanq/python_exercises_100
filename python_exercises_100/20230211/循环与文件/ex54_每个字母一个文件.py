"""
编写代码，
1、在当前目录下新建一个目录，名字为 p054
2、给26个英文字母在p054目录下生成一个文件，文件名分别是a.txt、b.txt ~~ z.txt，文件内容分别是字母a、b~~z
"""
# 方法一、使用循环写入
# import string
# for i in string.ascii_lowercase:
#     file = f'p054/{i}.txt'
#     with open(file,'w') as f:
#         f.write(i)
# 方法二、使用函数
import os
import string

if not os.path.exists("p055"):
  os.makedirs("p055")

for letter in string.ascii_lowercase:
  with open(f"p055/{letter}.txt", "w") as f:
    f.write(letter)
