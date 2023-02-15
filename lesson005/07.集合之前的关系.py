# Python 学习
# hqzhu
# 开发时间：23/2/11 16:13
'''相等'''
s1={10,20,30,40}
s2={10,30,20,40}
print(s1==s2)
'''子集'''
s1={10,20,30,40}
s2={10,20,40}
s3={10,90}
print(s2.issubset(s1))
print(s3.issubset(s1))
'''超集'''
print(s1.issuperset(s2))
print(s1.issuperset(s3))
'''是否有交集'''
print(s2.isdisjoint(s3))
s4={100,300,500}
print(s2.isdisjoint(s4))