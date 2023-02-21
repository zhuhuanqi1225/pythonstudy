# Python 学习
# hqzhu
# 开发时间：23/2/20 18:31

'''
类是个蓝图
实例是根据蓝图创建的产品
方法就是用产品，必须有产品才能操作，所以类必须实例化才能用

'''

class study_me():
    a=1

    def __init__(self,b,c):     #__init__代表此函数是study_me类的私有函数.self代表study_me本身
        self.b = b      #self.b，意思就是类内部私有化的变量
        self.c = c

    def add(self):
        return self.b + self.c
    def add_a():
        a +=1


haha = study_me(222,333)    #b=222,c=333

print(haha.a)           #a=1
print(haha.add())       #555
print(study_me.a)       #a=1