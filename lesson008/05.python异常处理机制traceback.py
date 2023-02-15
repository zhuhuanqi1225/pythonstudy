# Python 学习
# hqzhu
# 开发时间：23/2/15 19:04
#print(10/0)
import traceback
try:
    print('------------------------------')
    print(10/0)
except:
    traceback.print_exc()