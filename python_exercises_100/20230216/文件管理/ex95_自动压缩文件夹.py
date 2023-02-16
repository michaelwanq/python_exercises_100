"""
提供任何一个目录地址，用python实现文件夹的压缩，压缩成zip格式

例如：dir = r"D:\workbench\ant-python-exercises-100p"
则会生成一个文件 r"D:\workbench\ant-python-exercises-100p.zip"

这个压缩文件是对这个目录的压缩结果
"""
import os
import zipfile


def do_zip_compress(dirpath):
    output_name = f"{dirpath}.zip"
    parent_name = os.path.dirname(dirpath)
    zip = zipfile.ZipFile(output_name, "w", zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            if str(file).startswith("~$"):
                continue
            filepath = os.path.join(root, file)
            writepath = os.path.relpath(filepath, parent_name)
            zip.write(filepath, writepath)
    zip.close()


dirpath = r"D:\workbench\ant-python-exercises-100p"
do_zip_compress(dirpath)
