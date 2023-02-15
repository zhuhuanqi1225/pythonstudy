# Python 学习
# hqzhu
# 开发时间：23/2/14 20:04

#try...except...else
try:
    a = int(input('请输入一个整数：'))
    b = int(input('请输入另一个整数：'))
    res = a / b
except BaseException as e:
    print('出错了',e)
else:
    print(res)
finally:
    print('无论结果如何，都执行')