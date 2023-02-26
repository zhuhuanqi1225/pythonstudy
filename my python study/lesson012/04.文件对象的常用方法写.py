# Python 学习
# hqzhu
# 开发时间：23/2/26 20:05
file=open('c.txt','a')
#file.write('hello')    #写字符串
lst=['java','go','python']  #写列表
file.writelines(lst)
file.close()