# Python 学习
# hqzhu
# 开发时间：23/2/14 18:47
#局部变量，在函数内定义的变量，只在函数内有效
def fun(a,b):
    c=a+b           #c就是局部变量，a，b为形参，作用范围也是函数内，相当于局部变量
    print(c)

#print(c)   函数体外执行会报错，应该超出了c变量的作用域

name='老师'       #name作用范围在函数内部和外部，全局变量
print(name)
def fun2():
    print(name)
fun2()

def fun3():
    global age      #函数内部用global声明，变为全局变量
    age = 20
    print(age)
fun3()
print(age)