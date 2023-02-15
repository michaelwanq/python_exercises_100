# favarite_dict = {}
# name_list = []
# favarite_list = []
# with open('p085.txt') as f:
#     for line in f:
#         name,favarites = line.strip().split()
#         favarite_dict['name'] = favarites

like_count = {}

with open("p085.txt", encoding='utf8') as fin:
    for line in fin:
        line = line[:-1]
        sname, likes = line.split(" ")
        like_list = likes.split(",")
        for like in like_list:
            if like not in like_count:
                like_count[like] = 0
            like_count[like] += 1

for key, value in like_count.items():
    print(key, value)
