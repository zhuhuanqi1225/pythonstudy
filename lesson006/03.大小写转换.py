# Python 学习
# hqzhu
# 开发时间：23/2/12 11:02
#字符串大小写转换后，产生新对象
s='hello,python'
a=s.upper()
print(a,id(a))
print(s,id(s))
print(s.lower(),id(s.lower()))
s2='hello,Python'

print(s2.swapcase())
print(s2.capitalize())
print(s2.title())