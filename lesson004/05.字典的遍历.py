# Python 学习
# hqzhu
# 开发时间：23/2/10 19:41
scores={'张三':100,'李四':98,'王五':45}

for item in scores:
    print(item,scores[item],scores.get(item))

#键不能重复，值可以重复

d={'张三':100,'张三':98,'张三':45}
print(d)

d={'name':'张三','fistname':'张三'}
print(d)