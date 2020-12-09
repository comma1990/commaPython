# author : comma
# date : 2020/10/15 10:43

import openpyxl
wb=openpyxl.Workbook('/Users/sun/PycharmProjects/commaPython/study/12306抢票/车站编号.xlsx')
sheet=wb.active
lst=[] #存取所有车站的名称及编号
for row in sheet.rows: # 遍历所有的行
    sub_list=[]
    for cell in row: # 遍历每一行中的单元格，每一行的结果放到sub_list中，再将sub_list添加到lst中
        sub_list.append(cell.value)
    lst.append(sub_list)
print(dict(lst)) #将列表转换成字典，后期根据字典的键查找值（即：根据车站名字查找代号）



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


# 打印水仙花数  个位数的3次方+十位数的三次方+百位数的三次方=本身
for item in range(1,1000):
    ge=item%10
    shi=item//10%10
    bai=item//100
    if ge**3+shi**3+bai**3==item:
        print(item,end='\t')
print('\n----------------------')

# #   打印26个字母
for item in range(26):
    print(chr(item + ord('a')), end='\t')

print('\n-------------------')

# 时间处理
import time
import datetime


def getAddMinutesTime():
    data = datetime.datetime.now()
    offset = datetime.timedelta(minutes=2)
    result = (data + offset).strftime('%Y-%m-%dT%H:%M:%S')
    return result


def getAddDaysTime():
    data = datetime.datetime.now()
    offset = datetime.timedelta(days=2)
    result = (data + offset).strftime('%Y-%m-%dT%H:%M:%S')
    return result


print(getAddMinutesTime())
print(getAddDaysTime())
