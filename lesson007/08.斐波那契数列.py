# Python 学习
# hqzhu
# 开发时间：23/2/14 19:07
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        res=fib(n-1)+fib(n-2)
        return res
print(fib(6))

#输出前6位数字
for i in range(1,7):
    print(fib(i))
