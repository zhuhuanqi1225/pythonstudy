# Python 学习
# hqzhu
# 开发时间：23/2/10 13:45

#切片，格式[start:stop:step]
#切片语法创建的新列表是原始列表的副本，因此对新列表的更改不会影响原始列表
lst=[10,20,30,40,50,60,70,80]

print(lst[1:6:2])

lst2=lst[2:6:1]
print(lst2)

#列表反向输出
print(lst[::-1])
print(lst[6:0:-2])

#判断指定元素在列表中是否存在
print('p' in 'python')
print('s' in 'python')
lst=[10,20,'python','hello']
print(10 in lst)
print(10 not in lst)
print('py' in lst)

for item in lst:
    print(item)
