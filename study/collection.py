# Author ： comma
# 日期 : 2020/10/15  06:37

#记录学习过程中常用的方法

#time模块
import time
print(time.time()) #打印当前时间的时间戳

print(time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime()))  #格式化当前时间为：2020-10-15T07:13:59

import datetime
#获取当前时间
now=datetime.datetime.now();
#时间偏移量
add=datetime.timedelta(minutes=10)
#当前时间+时间偏移量
data=now+add
print(data.strftime('%Y-%m-%d %H:%M:%S')) #格式化时间



