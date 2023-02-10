"""
编写代码，生成文件p053.txt，每一行是三个英文字母的组合：
abc
def
ghi
jkl
mno
pqr
stu
vwx
yz
"""
import string

letters = string.ascii_lowercase + " "

slice1 = letters[0::3]
slice2 = letters[1::3]
slice3 = letters[2::3]

with open("p053.txt", "w") as file:
  for s1, s2, s3 in zip(slice1, slice2, slice3):
    file.write(s1 + s2 + s3 + "\n")
