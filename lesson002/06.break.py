# Python 学习
# hqzhu
# 开发时间：23/2/7 19:57

#从键盘录入密码，最多3次，如果正确就结束循环(for 和 while循环都可以使用break退出循环体)
'''
for item in range(3):
    pwd=input("请输入密码：")
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
'''
a=0
while a<3:
    pwd=input("请输入密码：")
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')

    a+=1