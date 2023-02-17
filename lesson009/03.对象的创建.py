# Python 学习
# hqzhu
# 开发时间：23/2/15 19:39
class Student:      #Student为类名，由一个或多个单词组成，首字母大写，其余小写
    native_pace='吉林'    #直接写在类里的变量，成为类属性

    def __init__(self,name,age):     #初始化方法
        self.name=name      #self.name成为实体属性，进行一个赋值操作，将局部变量name的值赋给实例属性
        self.age=age

    def eat(self):          #实例方法（类之外定义的是函数，类里面定义的是方法）
        print('学生在吃饭。。。')

    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')
    #类方法
    @classmethod
    def cm(cls):
        print('我使用了classmethod进行修饰，所以我是类方法')

print('-----------------以上是创建类-----------------------')

#创建Student类的对象
stu1=Student('张三',20)
print(id(stu1))         #stu1实例对象
print(type(stu1))
print(stu1)
print('===================================')
print(id(Student))      #Student类对象
print(type(Student))
print(Student)
print('-----------------以上是创建类的对象-----------------------')
#使用Student的类的方法