# Python 学习
# hqzhu
# 开发时间：23/2/21 19:38
class car():
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print('汽车已启动')

car = car('宝马X5')

car.start()
print(car.brand)