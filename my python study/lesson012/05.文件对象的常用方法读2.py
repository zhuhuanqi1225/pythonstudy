# Python 学习
# hqzhu
# 开发时间：23/2/26 20:05
file=open('a.txt','r')
file.seek(2)        #跳过2个字节开始读
print(file.read())
print(file.tell())  #返回当前光标位置
file.close()