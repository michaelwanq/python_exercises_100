"""
完成如下脚本代码：
a = [1, 2, 3]
产生如下输出：
Item 1 has index 0
Item 2 has index 1
Item 3 has index 2
"""
a = [1, 2, 3]
for i in range(0,len(a)):
    print(f'Item {a[i]} has index {i}')