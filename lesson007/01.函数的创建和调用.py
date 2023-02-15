# Python 学习
# hqzhu
# 开发时间：23/2/13 18:28

def calc(a,b):  #a，b形式参数，形参，函数定义处
    c=a+b
    return c
result=calc(10,20)  #10,20实际参数，实惨，函数调用处#按位置传参
print(result)

res=calc(b=30,a=20)  #按关键字a，b传参
print(res)