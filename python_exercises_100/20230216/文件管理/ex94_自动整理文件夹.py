"""
自己新建一个目录 arrange_dir
自己在文件夹下，手动新建多个“假文件”：
aaa.txt bbb.mp3 ccc.avi ccc.jpg ddd.jpg eee.txt fff.mp3 ggg.jpg hhh.txt iii.mp3
编写代码，按后缀名将文件移动到 arrange_dir 下的多个子目录，如下效果所示
"""
import os
import shutil

dir = "./arrange_dir"

for file in os.listdir(dir):
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    if not os.path.isdir(f"{dir}/{ext}"):
        os.mkdir(f"{dir}/{ext}")

    source_path = f"{dir}/{file}"
    target_path = f"{dir}/{ext}/{file}"
    shutil.move(source_path, target_path)
