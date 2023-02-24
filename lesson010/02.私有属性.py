# Python 学习
# hqzhu
# 开发时间：23/2/21 19:51
class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age        #age不希望在类外部使用，所以加了两个下划线在前面
    def show(self):
        print(self.name,self.__age)

stu = Student('张三',20)
stu.show()      #show是在类内部使用__age,所以可以调用
print(stu.name)
# print(stu.__age)        #__age无法在类外部直接使用
print(dir(stu))
print(stu._Student__age)    #无法使用的对象，可以通过_Student__age使用
