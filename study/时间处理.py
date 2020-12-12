#author : comma
#date : 2020/10/15 14:19

import time
import datetime

def demo():
    print(int(round(time.time() * 1000)))  # round()四舍五入，*1000是毫秒，获取毫秒的时间戳(13位)

#当前时间+n分钟
def getAddMinutesTime():
    data=datetime.datetime.now()
    offset=datetime.timedelta(minutes=2)
    result=(data+offset).strftime('%Y-%m-%dT%H:%M:%S') # 时间格式化
    return result

#当前时间+n天
def getAddDaysTime():
    data=datetime.datetime.now()
    offset=datetime.timedelta(days=7)
    result=(data+offset).strftime('%Y-%m-%dT%H:%M:%S')
    return result

#当前时间+n小时
def getAddHoursTime():
    data=datetime.datetime.now()
    offset=datetime.timedelta(hours=2)
    result=(data+offset).strftime('%Y-%m-%dT%H:%M:%S')
    return result

if __name__ == '__main__':
    getAddHoursTime()