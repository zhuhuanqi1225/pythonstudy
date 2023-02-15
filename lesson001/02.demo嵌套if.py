# Python 学习
# hqzhu
answer=input('您是会员吗？y/n')
money=float(input('购物金额是：'))

if answer=='y':
    print('会员')
    if money>=200:
        print('打8折，付款金额为：',money*0.8)
    elif money>=100:
        print('打9折，付款金额为：', money*0.9)
    else:
        print('不打折，付款金额为：', money)
else:
    print('非会员')
    if money>=200:
        print('打95折，付款金额为：',money*0.95)
    else:
        print('不打折，付款金额为：', money)
