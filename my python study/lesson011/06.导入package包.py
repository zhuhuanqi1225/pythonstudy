# Python 学习
# hqzhu
# 开发时间：23/2/25 20:45
#导入包package1中的模块moduleA，并起别名为A

import package1.moduleA as A    #导入包package1中的模块moduleA，并起别名为A
print(A.a)

'''
使用import导入时，只能跟包名和模块名
使用from *** import ***，可以导入包、模块、函数名、变量名a等
'''
from package1.moduleA import a
print(a)