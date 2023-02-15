# Python 学习
# hqzhu
# 开发时间：23/2/11 14:45
'''第一种，使用()'''
t=('python','world',98)
print(t,type(t))

t2='python','world',98  #小括号可省略（只包含一个元素时，需要使用逗号和小括号）
t3=('python')   #只包含一个元素时，逗号不能省
print(t2,type(t2))
print(t3,type(t3),)


'''第一种，使用内置函数tuple()'''
t1=tuple(('python','world',98))
print(t1,type(t1))

'''空元组'''
t4=()
t5=tuple()
print(t4,t5)

