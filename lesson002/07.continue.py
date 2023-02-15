# Python 学习
# hqzhu
# 开发时间：23/2/7 20:11

#输出1-50之间所有5的倍数
for item in range(1,51):
    if item%5==0:
        print(item)

print('========================================')

for item2 in range(1,51):
    if item2%5!=0:
        continue
    print(item2)
