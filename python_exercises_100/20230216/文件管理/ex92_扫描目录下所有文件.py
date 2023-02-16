"""
提供一个目录路径，用python扫描所有的文件，列出文件路径
dir = r"D:\workbench\ant-python-exercises-100p"
输出内容：
D:\workbench\ant-python-exercises-100p\.gitignore
D:\workbench\ant-python-exercises-100p\LICENSE
D:\workbench\ant-python-exercises-100p\Python入门练习100题课件.pptx
D:\workbench\ant-python-exercises-100p\README.md
等等
"""
import os

dir = r"D:\python\python_exercises_100\python_exercises_100\20230215\文件处理统计"
for root, dirs, files in os.walk(dir):
    # print(root)
    # print(dirs)
    # print(files)
    for file in files:
        fpath = os.path.join(root, file)
        print(fpath)

