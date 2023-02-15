# Python 学习
# hqzhu
# 开发时间：23/2/11 16:22

s1={10,20,30,40}
s2={20,40,30,50,60}
#交集
print(s1.intersection(s2))  #交集
print(s1 & s2)      #交集
#并集
print(s1.union(s2)) #并集去重
print(s1 | s2)  #并集去重

'''交并集不影响原集合数据'''

#差集操作
print(s1.difference(s2))    #s1减去s2中的的元素
print(s1 - s2)  #s1减去s2中的的元素

#对称差集
print(s1.symmetric_difference(s2))  #s1和s2的并集减去交集