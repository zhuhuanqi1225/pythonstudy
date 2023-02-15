# Python 学习
# hqzhu
# 开发时间：23/2/11 16:32
#列表生成式
lst=[i for i in range(1,10)]
print(lst)

'''列表中元素为2,4,6,8,10'''
lst2=[i*2 for i in range(1,6)]
print(lst2)
#集合生成式
s={i*i for i in range(6)}
print(s,type(s))