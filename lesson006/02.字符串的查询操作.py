# Python 学习
# hqzhu
# 开发时间：23/2/12 10:56
#字符串的查询
s='hello,hello'
print(s.index('lo'))    #'lo'第一次出现的位置，查不到报错
print(s.find('lo'))     #'lo'第一次出现的位置，查不到抛-1，推荐
print(s.rindex('lo'))   #'lo'最后一次出现的位置，查不到报错
print(s.rfind('lo'))    #'lo'最后一次出现的位置，查不到抛-1，推荐
