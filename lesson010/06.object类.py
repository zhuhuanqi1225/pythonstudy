# Python 学习
# hqzhu
# 开发时间：23/2/21 20:55
#object类是所有类的父类
class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0}，今年{1}岁了'.format(self.name,self.age)
stu = Student('张三',20)
print(dir(stu))
print(stu)          #默认调用__str__方法

#Object类有一个__str__()方法，用于返回一个对于“对象的描述”，对应于内置函数str()经常用于print方法，
# 帮助我们查看对象的信息，所以我们经常会对__str__进行重写