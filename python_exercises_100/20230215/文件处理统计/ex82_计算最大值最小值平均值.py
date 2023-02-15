"""
输入一个成绩文件，计算成绩的最大值最小值平均值
文件名：p082.txt，自己复制如下内容进去即可：
"""
# 方法一
# results = []
# with open('p082.txt') as f:
#     for line in f.readlines():
#         number, name, result = line.strip().split(',')
#         results.append(int(result))
#     max = max(results)
#     min = min(results)
#     average = sum(results) / len(results)
#     print('本次考试的最高分是： ', max)
#     print('本次考试的最高分是： ', min)
#     print('本次考试的最高分是： ', average)


# 方法二
def compute_score():
    scores = []
    with open("p082.txt") as fin:
        for line in fin:
            line = line.strip()
            fields = line.split(",")
            scores.append(int(fields[-1]))
    max_score = max(scores)
    min_score = min(scores)
    avg_score = round(sum(scores) / len(scores), 2)
    return max_score, min_score, avg_score


max_score, min_score, avg_score = compute_score()
print(max_score, min_score, avg_score)
