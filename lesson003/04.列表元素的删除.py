# Python 学习
# hqzhu
# 开发时间：23/2/10 14:34

#remove删除列表中元素，只删除第一个
lst=[10,20,30,40,50,60,30]
lst.remove(30)
print(lst)
#根据索引移除pop()
lst.pop(1)
print(lst)
lst.pop()       #如果不指定参数，删除最后一个元素
print(lst)
#切片，一次删除多个元素
print('------------------------------')
lst2=lst[1:3]
print(lst2)
print(lst)
lst[1:3]=[] #切掉1:3
print(lst)
#clear清除列表元素,del删除列表
lst.clear()
print(lst)

del lst
print(lst)