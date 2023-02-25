# Python 学习
# hqzhu
# 开发时间：23/2/25 21:02
#pip install schedule #需要配置环境变量，不然会报错
import schedule
import time
def job():
    print('哈哈--------')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)