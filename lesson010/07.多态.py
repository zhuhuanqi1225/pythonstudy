# Python 学习
# hqzhu
# 开发时间：23/2/22 19:22
class Animal(object):
    def eat(self):
        print('动物会吃')
class dog(Animal):
    def eat(self):
        print('狗吃肉')
class cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Person(object):
    def eat(self):
        print('人吃五谷杂粮')

#定义一个函数
def fun(obj):
    obj.eat()

#开始调用函数fun
fun(dog())
fun(cat())
fun(Animal())
print('======================')
fun(Person())