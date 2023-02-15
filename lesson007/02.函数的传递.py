# Python 学习
# hqzhu
# 开发时间：23/2/13 18:51
def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1',arg1)
    print('arg2',arg2)

n1=11
n2=[22,33,44]
print('n1',n1)
print('n2',n2)
fun(n1,n2)      #实参名称和形参名称可以不一致
print('n1',n1)  #11
print('n2',n2)  #[22, 33, 44, 10]

'''函数调用过程中，进行参数传递
如果是不可变对象，在函数体内修改时，不影响实参的值
如果是可变对象，在函数体内修改时，会影响实参的值
'''