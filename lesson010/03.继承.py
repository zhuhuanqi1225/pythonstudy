# Python 学习
# hqzhu
# 开发时间：23/2/21 20:01
class Person():     #Person是父类
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,no):
        super().__init__(name,age)      #从父类继承name,age
        self.no = no                    #自有no

class   Teacher(Person):
    def __init__(self,name,age,tyear):
        super().__init__(name,age)      #从父类继承name,age
        self.tyear = tyear              #自有tyear

stu1=Student('张三',20,1001)
tea1=Teacher('李四',34,12)

stu1.info()
tea1.info()