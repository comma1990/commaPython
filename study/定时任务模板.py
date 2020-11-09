# author : comma
# date : 2020/11/6 17:38

import schedule  # 定时任务模块
import time


def job():
    print("哈哈哈~~~~")


schedule.every(1).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
