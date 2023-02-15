# Python 学习
# hqzhu
# 开发时间：23/2/12 17:07

s='天涯共此时'
#编码
print(s.encode(encoding='GBK')) #GBK中，一个中文占2个字节
print(s.encode(encoding='UTF-8'))   #UTF-8，一个中文占3个字节
#解码(bytes代表一个二进制数据)
byte=s.encode(encoding='GBK')   #编码
print(byte.decode(encoding='GBK'))  #解码

byte=s.encode(encoding='UTF-8')   #编码
print(byte.decode(encoding='UTF-8'))  #解码
