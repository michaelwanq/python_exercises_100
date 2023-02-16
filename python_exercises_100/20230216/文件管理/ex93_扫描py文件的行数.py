"""
提供一个目录路径，用python找出所有的.py文件
展示文件路径，以及文件的行数
dir = r"D:\workbench\ant-python-exercises-100p"
输出内容：
D:\workbench\ant-python-exercises-100p\ceshi01.py 1
D:\workbench\ant-python-exercises-100p\p001.py 5
D:\workbench\ant-python-exercises-100p\p002.py 4
D:\workbench\ant-python-exercises-100p\p003.py 4
D:\workbench\ant-python-exercises-100p\p004.py 3
D:\workbench\ant-python-exercises-100p\p005.py 3
"""
import os

dir = r"D:\python\python_exercises_100\python_exercises_100\20230216\文件管理"
for root, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith(".py"):
            fpath = os.path.join(root, file)
            with open(fpath, encoding="utf8") as f:
                print(fpath, len(f.readlines()))
