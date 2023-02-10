"""
完成如下脚本代码：
a = [1, 2, 3]
产生如下输出：
Item 1 has index 0
Item 2 has index 1
Item 3 has index 2
"""
# 方法一、使用循环取列表的索引和对应的值进行打印
# a = [1, 2, 3]

# for i in range(0,len(a)):
#     print(f'Item {a[i]} has index {i}')
# 方法二、使用enumerate()获得下标和列表元素值对
a = [1, 2, 3]

for index, item in enumerate(a):
    print(f"Item {item} has index {index}")