# Python 学习
# hqzhu
# 开发时间：23/2/12 11:20
s='hello world python'
print(s.split())
s1='hello|world|python'
print(s1.split(sep='|'))    #sep指定分隔符
print(s1.split(sep='|',maxsplit=1))     #maxsplit指定最大劈分次数
#右劈分
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|',maxsplit=1))