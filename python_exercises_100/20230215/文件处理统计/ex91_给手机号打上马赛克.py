"""
如下文字中，有一些手机号数字
用python将所有的手机号，只保留开始和结尾数字，中间用******代替
白日依19989881888山尽，黄河入45645546468798978海流。
欲穷12345千里目，更上15619292345一层楼。
输出内容：
白日依19******88山尽，黄河入45645546468798978海流。
欲穷12345千里目，更上15******45一层楼。
"""
import re

pattern = r"(1\d)\d{7}(\d{2})"

print(re.sub(pattern, r"\1******\2", content))


