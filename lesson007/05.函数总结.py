# Python 学习
# hqzhu
# 开发时间：23/2/13 19:56
def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

fun(10,20,30)
'''报错
lst=[10,20,30]
fun(lst)
'''
lst=[10,20,30]
fun(*lst)   #*号，在函数调用时，将列表中的每个元素都转换为位置实参传入

fun(a=100,b=200,c=300)  #关键字实参调用

dic={'a':111,'b':222,'c':333}
#fun(dic)   报错
fun(**dic)  #**号，在函数调用时，将字典中的键值对都转换为关键字实参传入


# 位置实参和关键字实参可以混合传递
def fun2(a,b,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
fun2(10,20,c=30,d=40)

'''需求，c和d只能采用关键字传递'''
def fun2(a,b,*,c,d):    #单独的一颗星*，*之后的参数在函数调用时只能采用关键字参数
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
fun2(10,20,c=30,d=40)

'''函数定义时的形参顺序问题'''
def fun5(a,b,*,c,d,**args):
    pass
def fun6(*args,**args2):
    pass
def fun7(a,b=10,*args,**args2):
    pass