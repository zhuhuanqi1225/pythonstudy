# Python 学习
# hqzhu
# 开发时间：23/2/7 19:28

# in表达遍历的对象
for item in ('python'):
    print(item)

for item2 in (range(1,10,2)):
    print(item2)
#不需要自定义变量的话，用下划线
for _ in (range(5)):
    print('python,hello')

#计算1-100的偶数和
sum=0
for item3 in range(1,101):
    if item3%2==0:
        sum+=item3
print('1-100之间偶数和为：',sum)