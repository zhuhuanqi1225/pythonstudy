# Python 学习
# hqzhu
# 开发时间：23/2/10 19:52
item=['fruite','books','others']
prices=[96,78,85]

d={item:price for item,price in zip(item,prices)}
print(d)