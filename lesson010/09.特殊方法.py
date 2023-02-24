# Python 学习
# hqzhu
# 开发时间：23/2/24 21:19
a=20
b=100
c=a+b   #两个整数类型的相加操作
print(c)

d=a.__add__(b)  #__add__，加
print(d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return  self.name+other.name
    def __len__(self):
        return len(self.name)

stu1=Student('jack')
stu2=Student('李四')

s=stu1+stu2     #实现两个对象的加法运算，因为在Student类中编写了__add()特殊方法
print(s)
R=stu1.__add__(stu2)
print(R)

lst=[11,22,33,44]
print(len(lst))         #len计算列表长度
print(lst.__len__())    #同上

print(stu1.__len__())   #