# Python 学习
# hqzhu
# 开发时间：23/2/7 20:40
#打印三行四列矩形
for i in range(1,4):    #行数
    for j in range(1,5):    #列数
        print('*',end='\t') #不换行输出
    print() #换行

#打印直角三角形
for i in range(1,10):   #行数
    for j in range(1,i+1):  #列数
        print('*',end='')
    print()

#打印九九乘法表

for i in range(1,10):   #行数
    for j in range(1,i+1):  #列数
        print(i,'*',j,'=',i*j,end='\t')
    print()