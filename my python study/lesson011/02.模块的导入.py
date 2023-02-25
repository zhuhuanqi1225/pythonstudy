# Python 学习
# hqzhu
# 开发时间：23/2/25 19:44

'''
import math     #数学运算模块
print(id(math))
print(type(math))
print(math)
print(dir(math))

print(math.pow(2,3),type(math.pow(2,3)))
print(math.ceil(9.001))
print(math.floor(9.99999))
'''

from math import pi
print(pi)
#print(math.pow(2,3))    #没有导入pow会报错

#单独导入后，不用使用math.，可以直接用