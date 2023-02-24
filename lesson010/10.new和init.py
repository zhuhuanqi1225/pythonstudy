# Python 学习
# hqzhu
# 开发时间：23/2/24 21:32
#__new__在前,__init__在后
class Person(object):

    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象obj的id为{0}'.format(id(obj)))
        return obj

    def __init__(self,name,age):
        print('__init__方法被调用了，self的id值为{0}'.format(id(self)))
        self.name=name
        self.age=age

print('object这个类对象的id为{0}'.format(id(object)))
print('Person这个类对象的id为{0}'.format(id(Person)))

#创建Person类的实例对象
p1 =Person('张三',20)
print('p1这个Person类的实例对象id{0}'.format(id(p1)))

'''
程序执行顺序：
1.执行Person('张三',20)，将Person的值传入Person类，__new__的cls
2.obj=super().__new__(cls)，将cls传入object类，在object里创建了对象obj
3.return obj，创建完obj输出，给了__init__的self
4.self再赋值给了p1
'''