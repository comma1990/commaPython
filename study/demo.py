#author : comma
#date : 2020/10/15 10:43


n=input('请输入你要创建活动的商品个数：')
x=0
def digui():
    for i in range(int(n)):
        if i!=3:
            x+=1
        if x!=0:
            digui()
        print(x)




# #   打印26个字母
# for item in range(26):
#     print(chr(item+ord('a')))

# 时间处理
# import time
# import datetime
# def getAddMinutesTime():
#     data=datetime.datetime.now()
#     offset=datetime.timedelta(minutes=2)
#     result=(data+offset).strftime('%Y-%m-%dT%H:%M:%S')
#     return result
#
# def getAddMinutesTime():
#     data=datetime.datetime.now()
#     offset=datetime.timedelta(days=2)
#     result=(data+offset).strftime('%Y-%m-%dT%H:%M:%S')
#     return result

