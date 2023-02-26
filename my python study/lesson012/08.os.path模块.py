# Python 学习
# hqzhu
# 开发时间：23/2/26 20:53
import os.path
print(os.path.abspath('01.编码格式.py'))    #输出文件绝对路径
print(os.path.exists('01.编码格式.py'),os.path.exists('assd.py'))   #判断文件是否存在
print(os.path.join('E:\\python','deom1.py'))    #拼接路径
print(os.path.split('C:\\个人文档\\我的学习\\python\\test01\\venv\\my python study\\lesson012\\01.编码格式.py'))    #拆分文件路径和文件名
print(os.path.splitext('01.编码格式.py'))    #拆分文件文件名和文件后缀
print(os.path.basename('C:\\个人文档\\我的学习\\python\\test01\\venv\\my python study\\lesson012\\01.编码格式.py')) #提取文件名
print(os.path.dirname('C:\\个人文档\\我的学习\\python\\test01\\venv\\my python study\\lesson012\\01.编码格式.py'))  #提取文件名的路径，不含文件名
print(os.path.isdir('C:\\个人文档\\我的学习\\python\\test01\\venv\\my python study\\lesson012\\01.编码格式.py'))  #判断是否路径

