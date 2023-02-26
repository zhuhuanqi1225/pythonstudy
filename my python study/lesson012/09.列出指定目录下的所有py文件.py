# Python 学习
# hqzhu
# 开发时间：23/2/26 21:06
import os
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith(('.py')):
        print(filename)