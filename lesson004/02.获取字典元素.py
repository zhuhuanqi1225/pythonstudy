# Python 学习
# hqzhu
# 开发时间：23/2/10 15:53

scores={'张三':100,'李四':98,'王五':45}
print(scores['张三'])

print(scores.get('张三'))
print(scores.get('陈六'))
print(scores.get('李六',99))  #99为查找李六不存在时，提供的默认值
