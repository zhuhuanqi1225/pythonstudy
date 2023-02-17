# Python 学习
# hqzhu
# 开发时间：23/2/15 19:32
#不同的数据类型属于不同的类
#实用内置函数可以查看数据类型
print(type(100))
#<class 'int'>
#int是类，100是类对象

class Student:      #Student为类名，由一个或多个单词组成，首字母大写，其余小写
    pass
print(id(Student))      #2412559732768
print(type(Student))    #<class 'type'>
print(Student)          #<class '__main__.Student'>