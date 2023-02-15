# Python 学习
# hqzhu
# 开发时间：23/2/14 18:54
#if 终止 else 调用
def fac(n):
    if n==1:
        return 1
    else:
        res=n*fac(n-1)
        return res
print(fac(6))
