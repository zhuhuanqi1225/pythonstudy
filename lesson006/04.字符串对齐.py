# Python 学习
# hqzhu
# 开发时间：23/2/12 11:10
'''
str.ljust(width[, fillchar])：返回一个原字符串左对齐，并使用空格填充至指定长度的新字符串。如果指定了 fillchar，则使用该字符进行填充。

str.rjust(width[, fillchar])：返回一个原字符串右对齐，并使用空格填充至指定长度的新字符串。如果指定了 fillchar，则使用该字符进行填充。

str.center(width[, fillchar])：返回一个原字符串居中，并使用空格填充至指定长度的新字符串。如果指定了 fillchar，则使用该字符进行填充。

'''

s='hello,Pyhon'
print(s.center(20,'*'))
print(s.ljust(20,'*'))
print(s.ljust(10,'*'))  #长度小于实际长度，输出元字符
print(s.rjust(20,'*'))
print(s.zfill(20))  #0填充