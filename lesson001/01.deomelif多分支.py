# Python 学习
# hqzhu

score=int(input('请输入你的成绩'))

if  90<=score<=100:
    print('A级')
elif 80<=score<90:
    print('B级')
elif 70<=score<80:
    print('C级')
elif 60<=score<70:
    print('D级')
elif 0<=score<60:
    print('不及格')
else:
    print('输入不合格式')