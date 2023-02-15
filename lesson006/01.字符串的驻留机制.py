# Python 学习
# hqzhu
# 开发时间：23/2/12 10:38
a='python'
b="python"
c='''python'''
print(a,id(a),type(a))
print(b,id(b),type(b))
print(c,id(c),type(c))  #a,b,c内存地址相同

s1=''
s2=''
print(s1==s2)
print(s1 is s2)
s1='abc%'
s2='abc%'
print(s1==s2)
print(s1 is s2)