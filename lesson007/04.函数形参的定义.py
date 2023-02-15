# Python 学习
# hqzhu
# 开发时间：23/2/13 19:31
#默认值参数
def fun(a,b=10): #b有默认值10
    print(a,b)

#函数调用
print(fun(100))

print(fun(101,22))

print('hello',end='\t')
print('world')
#个数可变的位置参数
def fun2(*args):    #参数个数只能定义一个
    print(args)
    print(args[0])

fun2(100)
fun2(100,200)
fun2(100,200,300)

#个数可变的关键字形参
def fun3(**args):   #参数个数只能定义一个
    fun(args)

fun3(a=10)
fun3(a=20,b=30,c=40)    #结果为字典

'''函数定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求位置形参放在关键字形参前面'''
def fun(*args1,**args2):
    pass

