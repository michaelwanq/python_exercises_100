"""
新建文件p081.txt，将如下内容粘贴到文件中
编写代码，给每个数字乘以2，结果输出到p081_output.txt
"""
# with open('p081.txt') as f:
#     for line in f.readlines():
#         x, y = line.strip().split(',')
#         print(x, y)

with open("p081.txt") as fin, open("p081_output.txt", "w") as fout:
    for line in fin:
        if "x,y" in line:
            fout.write(line)
        else:
            x, y = line.strip().split(",")
            x = int(x) * 2
            y = int(y) * 2
            fout.write(f"{x},{y}\n")
