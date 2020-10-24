#author : comma
#date : 2020/10/15 10:43




########列表的操作：#################
# 排序
# list1=[0,9,5,7,2,3]
# list1.sort()    # 升序
# list1.sort(reverse=True)    # 倒序
# print(list1)
#print(sorted(list1))    # 内置函数
#print(sorted(list1,reverse=True))   # 先升序排序，然后翻转，就是倒序

# 列表表达式
# list2=[i*i for i in range(1,10,2)]  # 范围1-10，步长为2，遍历结果是1，3，5，7，9；遍历结果自相乘
# print(list2)
####################################


# #空列表的bool值为False
# x=[]
# print(bool(x))


# n=int(input('请输入次数'))
# x=100
# i=0
# while i<n:
#     x=x/2
#     i+=1
# print(x)


# 打印9*9乘法表
# for x in range(1,10):
#     for y in range(1,x+1):
#         print(x,'*',y,'=',x*y,end='\t')
#     print()


# 打印水仙花数
# for item in range(1,1000):
#     ge=item%10
#     shi=item//10%10
#     bai=item//100
#     if ge**3+shi**3+bai**3==item:
#         print(item,end='\t')




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

