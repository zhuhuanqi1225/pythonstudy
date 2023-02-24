# Python 学习
# hqzhu
# 开发时间：23/2/24 22:22
class CPU:
    pass
class Disk:
    pass
class Cumputer:
    def __init__(self,cpu,disk):
        self.cpu =cpu
        self.disk=disk
#变量的赋值
cpu1 =CPU()
cpu2=cpu1
print(cpu1)
print(cpu2)
#cpu1和cpu2内存地址相同，是同一个对象，放到两个变量中

#浅拷贝
print('=================================')
disk = Disk()   #创建硬盘类对象
computer=Cumputer(cpu1,disk)    #创建一个计算机类对象

import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
'''
cpu1和disk不拷贝，内存地址不变，只拷贝computer，computer2内存地址不同
'''

print('===============================')
#深拷贝
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)
'''
cpu1和disk都不拷贝，内存地址变化，拷贝computer3以及子类cpu和disk内存地址都跟之前不同
'''