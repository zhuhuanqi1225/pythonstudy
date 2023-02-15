# Python 学习
# hqzhu
# 开发时间：23/2/6 21:13

# 计算1-100的偶数和

sum=0 # 用于存储偶数
a =1
while a<=100:
    if not bool(a%2):# 同if a%2==0:
        sum+=a
    a+=1
print('和为',sum)

# 计算1-100的奇数和

sum=0 # 用于存储偶数
a =1
while a<=100:
    if a%2:
        sum+=a
    a+=1
print('和为',sum)
