# Python 学习
# hqzhu
# 开发时间：23/2/26 19:50
file=open('a.txt','r')
print(file.readlines())
file.close()

file=open('b.txt','w')      #w写文件,没有就创建。有就替换
file.write('python')
file.close()

file=open('b.txt','a')      #a写文件,没有就创建。有就追加
file.write('python')
file.close()
