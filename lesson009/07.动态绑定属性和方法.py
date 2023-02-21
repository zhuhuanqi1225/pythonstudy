# Python 学习
# hqzhu
# 开发时间：23/2/21 19:02
#python是动态语言，在创建对象后，可以动态的绑定属性和方法
class Student:
    def __init__(self,name,age):        #self.name和self.age，是改类下所有实例共有的
        self.name = name
        self.age = age
    def eat(self):
        print(self.name+'在吃饭')

stu1= Student('张三',20)      #stu1是Student类的实例对象
stu2= Student('李四',30)      #一个Student类可以创建多个实例对象，每个实例可以不同

print('=================为stu2动态绑定性别属性=======================')
#只给李四添加性别gender=女
stu2.gender = '女'
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)   #gender属性只归属stu2

#eat是定义在类里的方法，所以是stu1和stu2共有
stu1.eat()
stu2.eat()

print('=================为stu1动态绑定show方法=======================')
def show():
    print('定义在类之外的，称为函数')
stu1.show = show
stu1.show()     #只有stu1有show方法