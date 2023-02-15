# Python 学习
# hqzhu
# 开发时间：23/2/12 15:57
s='hello,python'
#判断字符串是不是合法的标识符
print(s.isidentifier())
print('hello'.isidentifier())
print('张三_'.isidentifier())
print('张三_123'.isidentifier())
#判断字符串是否全部由空白字符组成
print(s.isspace())
print('\t'.isspace())
#判断是否全部由字母组成
print('abc'.isalpha())
print('abc1'.isalpha())
print('张三'.isalpha())
#是否全部由十进制组成
print('1234'.isdecimal())
print('123f'.isdecimal())
#是否全部由数字组成（罗马数字，汉语数字true）
print('12345'.isnumeric())
print('1234五'.isnumeric())
#是否全部由字母和数字组成
print('abc1'.isalnum())
print('abc测试123'.isalnum())
print('abc!'.isalnum())