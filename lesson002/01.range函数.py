# Python 学习
# hqzhu
# 开发时间：23/2/6 20:34

# range三种方式（不管长度多少，占内存相同，因为只存储“起始值，终结值，步长”三个值）
# 1
r=range(10)
print(r)  # ange(0, 10)
print(list(r))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，默认0开始步长1
# 2
r=range(1,10)
print(list(r))   # [1, 2, 3, 4, 5, 6, 7, 8, 9]，1开始10结束步长1
# 3
r=range(1,10,2)  # [1, 3, 5, 7, 9]，1开始10结束步长2
print(list(r))

# in 和not in
print(10 in r)
print(9 in r)
print(10 not in r)
print(9 not in r)
