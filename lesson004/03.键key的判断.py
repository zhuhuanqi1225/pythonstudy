# Python 学习
# hqzhu
# 开发时间：23/2/10 19:29
scores={'张三':100,'李四':98,'王五':45}
print('张三' in scores)
print('张三' not in scores)

#删除键值对
del scores['张三']
print(scores)
#clear清空字典元素
print(scores.clear())
#新增字典元素
scores['陈六']=98
print(scores)
#修改字典元素
scores['陈六']=100
print(scores)