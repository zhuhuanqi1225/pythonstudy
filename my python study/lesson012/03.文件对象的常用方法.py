# Python 学习
# hqzhu
# 开发时间：23/2/26 20:05
file=open('a.txt','r')
#print(file.read())      #读取全部
print(file.read(2))    #读取前2个
#print(file.readline())      #读取一行
#print(file.readlines())      #读取全部，每行作为独立的列表中的元素
#print(file.readlines())
file.close()