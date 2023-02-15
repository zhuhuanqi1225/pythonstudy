# Python 学习
# hqzhu
# 开发时间：23/2/7 19:40

#输出100-999之间的水仙花数。水仙花数153=3*3*3+5*5*5+1*1*1

for item in range(100,1000):
    ge=item%10  # %求余数，得到个位数
    shi=item//10%10 #//整除，得到十位数
    bai=item//100 #//整除，得到百位数
    if ge**3+shi**3+bai**3==item:   #**幂运算
        print(item)