# Python 学习
# hqzhu
# 开发时间：23/2/26 20:37
#os模块与操作系统相关的模块
import os
#os.system('notepad.exe')    #调用系统，打开notepad
#直接调用可执行文件
#os.startfile('C:\\Program Files (x86)\\Tencent\\QQ\\Bin\\qq.exe')
print(os.getcwd())  #输出当前文件路径

lst=os.listdir('../lesson012')  #返回指定路径下的文件和目录信息
print(lst)

#os.mkdir('newdir')      #创建目录
#os.makedirs('A/B/C')    #创建多级目录
#os.rmdir('newdir')      #删除目录
os.removedirs('A/B/C')  #删除多级目录
