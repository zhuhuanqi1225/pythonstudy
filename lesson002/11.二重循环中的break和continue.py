# Python 学习
# hqzhu
# 开发时间：23/2/7 20:59

#二重循环中的break和continue只影响本层循环

for i in range(5):
    for j in range(1,10):
        if j%2==0:
            break
        print(j)
print('======================')

for i in range(5):
    for j in range(1,10):
        if j%2==0:
            continue
        print(j,end='\t')
    print()
