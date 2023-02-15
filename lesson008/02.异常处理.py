# Python 学习
# hqzhu
# 开发时间：23/2/14 19:52
#try...except
try:
    a = int(input('请输入一个整数：'))
    b = int(input('请输入另一个整数：'))
    res = a / b
    print('结果为：', res)
except ZeroDivisionError:
    print('除数不能为零')
except ValueError:
    print('只能输入数字')

