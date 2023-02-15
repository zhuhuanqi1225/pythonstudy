# Python 学习
# hqzhu
# 开发时间：23/2/13 19:14
def fun(num):
    odd=[]  #存奇数
    even=[] #存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

#调用函数
lst=[10,29,34,23,44,53,55]
lst2=fun(lst)
print(lst2)


# 1.如果函数没有返回值，可以不写return
def fun():
    print('hello')
fun()
#2.如果返回值是1个，直接返回原值，需要赋值存储
def fun2():
    return 'hello'
f=fun2()
print(f)
#3.如果返回值是多个，返回元组
def fun3():
    return 'hello','world'
fu=fun3()
print(fu)

'''函数在定义时，是否需要返回值，视情况而定'''