# Author ： comma
# 日期 : 2020/10/15  07:22
import time
import datetime
# 获取时间的方法

# 1.获取当前时间
def getNowTime():
    return time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime())
# 2、获取当前时间+2分钟
def getAddMinutesTime():
    now=datetime.datetime.now()
    offset=datetime.timedelta(minutes=2) # 时间偏移量+2
    data=now+offset
    #print(data.strftime('%Y-%m-%dT%H:%M:%S'))
    return data.strftime('%Y-%m-%dT%H:%M:%S')

# 3、获取当前时间+7天
def getAddDaysTime():
    now=datetime.datetime.now()
    offset=datetime.timedelta(days=7) # 时间偏移量+2
    data=now+offset
    #print(data.strftime('%Y-%m-%dT%H:%M:%S'))
    return data.strftime('%Y-%m-%dT%H:%M:%S')

if __name__ == '__main__':
    print(getAddMinutesTime())