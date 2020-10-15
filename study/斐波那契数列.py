# author : comma
# date : 2020/10/14 12:28
import requests
import urllib3
import json


month = int(input('繁殖几个月？： '))
month_1 = 1  # 一月大的兔子初始值为1对
month_2 = 0  # 二月大的兔子初始值为0对
month_elder = 0  # 成年兔

for i in range(month):
    # 第一个月 一月兔刚刚出生,所以跳过
    if i != 0:
        # temp_1 = month_1
        # temp_2 = month_2
        # temp_elder = month_elder
        # month_1 = temp_elder + temp_2
        # month_2 = temp_1
        # month_elder = temp_elder + temp_2
        month_1, month_2, month_elder = month_elder+month_2, month_1, month_elder+month_2  # 等效与上面六行代码
    print('第%d个月共' % (i + 1), month_1 + month_2 + month_elder, '对兔子')
    print('其中1月兔：', month_1)
    print('其中2月兔：', month_2)
    print('其中成年兔：', month_elder)