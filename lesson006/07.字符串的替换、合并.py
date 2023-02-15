# Python 学习
# hqzhu
# 开发时间：23/2/12 16:06
s='hello,python'
print(s.replace('python','java'))
s1='hello,python,python,python'
print(s1.replace('python','java',2))

#合并（join()将列表或者元组中的字符合并成字符串）
lst=['hello','java','python']

print('|'.join(lst))
print(''.join(lst))

t=('hello','java','python')
print(''.join(t))

print('*'.join('python'))