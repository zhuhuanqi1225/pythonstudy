# Python 学习
# hqzhu

num_a=int(input('请输入第一个整数'))
num_b=int(input('请输入第二个整数'))
# 比较大小
'''
if num_a >=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)
'''
# 同上，使用条件表达式
print( (str(num_a)+'大于等于'+str(num_b)) if num_a>=num_b  else (num_a,'小于',num_b))
# 中间的条件表达式（if num_a>=num_b）如果是true则执行左侧，false的执行右侧