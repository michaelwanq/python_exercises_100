"""
如下文字中，有很多电话号码，用python提取打印出来
白日依19989881888山尽，黄河入45645546468798978海流。
欲穷12345千里目，更上15619292345一层楼。
"""
import re

content = """
白日依19989881888山尽，黄河入45645546468798978海流。
欲穷12345千里目，更上15619292345一层楼。
"""
pattern = r"1\d{10}"
results = re.findall(pattern, content)

for result in results:
    print(result)
