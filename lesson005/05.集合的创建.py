# Python 学习
# hqzhu
# 开发时间：23/2/11 15:09
'''第一种创建方式{}'''
s={2,3,4,5,5,6,7,7}     #元素不允许重复
print(s)
'''第二种创建方式，set()'''
s1=set(range(6))
print(s1,type(s1))

s2=set([1,2,3,4,3,6])
print(s2,type(s2))

s3=set((1,2,3,2,3,4,5,16))
print(s3,type(s3))

s4=set('python')    #集合中元素是无序的
print(s4,type(s4))

s5=set({12,2,3,43,54})
print(s5,type(s5))

s6=set()
print(s6,type(s6))
