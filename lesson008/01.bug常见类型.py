# Python 学习
# hqzhu
# 开发时间：23/2/14 19:22
age=input('请输入你的年龄：')
print(type(age))
#if age>=18:
if int(age)>=18:
    print('成年人')


'''
1.漏了末尾冒号
2.缩进错误
3.中英文符号
4.字符串拼接时，把字符串和数字拼接在一起
5.没有定义变量，比如while循环的变量
6.==和=搞混
7.索引越界  lst=[11,22,33,44]   print(lst[4])
8.append不熟  lst=[] lst=append('a','b','c')  print(lst)  append是list的方法，所以应该用lst.append，且append每次只能添加一个元素
'''