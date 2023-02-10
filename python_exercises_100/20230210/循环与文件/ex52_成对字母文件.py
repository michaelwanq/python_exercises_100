"""
编写代码，生成文件p052.txt，每一行是两个英文字母的组合：
ab
cd
ef
...
yz
"""
import string

with open("p052.txt", "w") as f:
  for i, j in zip(string.ascii_lowercase[::2], string.ascii_lowercase[1::2]):
    f.write(i + j + "\n")