# Python 学习
# hqzhu
# 开发时间：23/2/11 15:22
''''''
#判断
s={10,20,30,40,50,60}
print(10 in s)  #True
print(100 in s) #False
print(20 not in s)  #False
print(100 not in s) #True
#新增
s.add(80)   #一次加一个
print(s)
s.update({200,300,400})     #一次加多个
print(s)
s.update([23,43,54])
s.update((54,65,76))
print(s)
#删除
s.remove(40)
print(s)
s.discard(1000) #如果不存在，不报错
print(s)
s.pop()     #随机删除
print(s)
s.clear()   #清空元素
print(s)