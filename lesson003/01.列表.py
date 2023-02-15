# Python 学习
# hqzhu
# 开发时间：23/2/8 19:59

#创建列表
#方式1
lst=['hello','world',98]
print(id(lst))
print(type(lst))
print(lst)
#方式2

lst2=list(['hello','world',98])
print(lst2)

#内存中，列表的value就是列表中各值对应的id

lst=['hello','world',98]

print(lst[0],lst[-3])

#获取列表中指定元素的索引

lst=['hello','world',98]

print(lst.index('hello'))
print(lst.index('hello',0,2))

#根据索引获取列表中的元素
lst=['hello','world',98,'hello','world',234]
print(lst[2])
print(lst[-3])
