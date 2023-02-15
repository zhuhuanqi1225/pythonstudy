# Python 学习
# hqzhu
# 开发时间：23/2/10 14:13

#添加到列表末尾append(),修改的是原始列表

lst=[10,20,30,40,50,60,70,80]
print(id(lst))
lst.append(100)
print(lst)
print(id(lst))

#extend()在列表末尾至少添加一个元素

lst2=['hello','world']
lst.append(lst2)
print(lst)
lst.extend(lst2)
print(lst)
#insert()在任意位置添加一个元素
lst.insert(1,90)
print(lst)
#在任意位置添加多个元素，相当于切掉start后面的
lst3=['aaa','bbb',666]
lst[1::]=lst3
print(lst)