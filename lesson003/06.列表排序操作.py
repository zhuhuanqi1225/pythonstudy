# Python 学习
# hqzhu
# 开发时间：23/2/10 14:56

#sort操作员列表排序
lst=[20,40,98,54]
print('排序前列表',lst,id(lst))

lst.sort()
print('升序排序后列表',lst,id(lst))
lst.reverse()
print('降序排序后列表',lst,id(lst))

#使用内置函数sorted(),产生新的列表对象
lst=[20,40,98,54]
lst2=sorted(lst)
print(lst2)

desc_lst= sorted(lst2,reverse=True)
print(desc_lst)