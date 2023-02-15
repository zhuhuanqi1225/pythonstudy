# Python 学习
# hqzhu
# 开发时间：23/2/12 16:16
s=''
print('apple'>'app')    #True
print('apple'>'banan')  #False
#比较的是原始值
print(ord('a'),ord('b'))
print(chr(97),chr(98))

'''==与is的区别（==比较value，is比较id）'''
a=b='python'
c='python'
print(a==b)
print(a==c)
print(a is b)
print(a is c)