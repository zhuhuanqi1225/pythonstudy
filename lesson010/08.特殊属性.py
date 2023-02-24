# Python 学习
# hqzhu
# 开发时间：23/2/24 21:05
print(dir(object))

class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age

#创建C类对象
x=C('JACK',20)     #x是C类的实例对象
print(x.__dict__)   #__dict__是查看（实例）对象，属性的字典

print(C.__dict__)   #查看类对象，属性和方法的字典
print('============================')
print(x.__class__)  #__class__输出对象所属的类
print(C.__bases__)  #__bases__，输出父类类型的元组
print(C.__base__)   #__base__，输出离他最近的父类
print(C.__mro__)    #__mro__，输出类的层级结构
print(A.__subclasses__())   #__subclasses__()输出所有子类列表