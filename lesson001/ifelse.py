#coding=utf-8
#代码文件：test01\not and or.py

score = int(input("请输入一个0~100的整数："))

if score>=60:
    if score>=85:
        print("您真优秀")
    else:
        print("您成绩还可以，但仍需要努力")
else:
    print("您需要加倍努力")