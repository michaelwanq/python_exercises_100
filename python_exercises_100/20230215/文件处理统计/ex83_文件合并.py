"""
用python编写代码，把这两个txt拼接在一个文件，存入p083.txt
"""
# 方法一
# with open('p083_xiaomei.txt',encoding='utf8') as f1,open('p083.txt','w') as f3:
#     message = f1.read()
#     f3.write(message)
# with open('p083_xiaohua.txt',encoding='utf8') as f2,open('p083.txt','a') as f3:
#     add_message = f2.read()
#     f3.write(add_message)

# 方法二
with open("p083.txt", "w", encoding='utf8') as fout:
    for fname in ["p083_xiaomei.txt", "p083_xiaohua.txt"]:
        with open(fname, encoding='utf8') as fin:
            for line in fin:
                fout.write(line)
