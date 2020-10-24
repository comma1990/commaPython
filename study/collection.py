# Author ： comma
# 日期 : 2020/10/15  06:37

# 记录学习过程中常用的方法
############random获取随机数##############
# import random
#
# print(random.random())  # 产生一个[0，1）之间的随机数
# print(random.randint(1, 20))  # 产生一个1-20之间的随机数
# print('-------')
# for i in range(1, 10):
#     print(random.randrange(2, 20, 2), end='\t')  # 产生一个[2,20)之间的随机数，步长为2，所以都是偶数
# print('------')
# lst = [1, 20, 23, 44, 87, 22, 11, 8, 30]
# print(random.choice(lst))  # 随机获取一个列表中的元素
# random.shuffle(lst)  # 打乱列表顺序
# print(lst)
################################################

# time模块
# import time
# print(time.time()) #打印当前时间的时间戳
#
# print(time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime()))  #格式化当前时间为：2020-10-15T07:13:59
#
# import datetime
# #获取当前时间
# now=datetime.datetime.now();
# #时间偏移量
# add=datetime.timedelta(minutes=10)
# #当前时间+时间偏移量
# data=now+add
# print(data.strftime('%Y-%m-%d %H:%M:%S')) #格式化时间
