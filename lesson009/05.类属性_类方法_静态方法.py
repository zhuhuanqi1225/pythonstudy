# Python 学习
# hqzhu
# 开发时间：23/2/16 19:41
class Student:      #Student为类名，由一个或多个单词组成，首字母大写，其余小写
    native_pace='吉林'    #直接写在类里且方法外的变量，成为类属性

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

#类属性的使用方式，类名调用
print(Student.native_pace)
#创建2个学生对象
stu1=Student('张三',20)
stu2=Student('李四',30)

print(stu1.native_pace)
print(stu2.native_pace)
#可以修改类属性
Student.native_pace='天津'
print(stu1.native_pace)
print(stu2.native_pace)

print('stu1的名称是：'+stu1.name)
print('stu2的年龄是：'+str(stu2.age))

#类方法的使用方式
print('-----------------以下是类方法的使用-----------------------')
Student.cm()


#静态方法的使用方式
print('-----------------以下是静态方法的使用-----------------------')
Student.method()

Student.eat(self=stu1)