# Python 学习
# hqzhu
# 开发时间：23/2/11 15:07

'''元组的遍历'''
t=('python','world',98)
'''第一种获取元组元素的方式，索引'''
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
'''遍历元组'''
for item in t:
    print(item)