#author : comma
#date : 2021/1/4 11:21


# dic={'逗号': 30, '二豆': 24, '憨憨': 26}
# print(dic.values())
# print(dic.keys())
# print(dic.items())
# print(list(dic.values()))
# print(list(dic.keys()))
# print(list(dic.items()))
# dic2={'渣渣':27}
# dic.update(dic2)
# print(dic)

import openpyxl
# import xlrd
# wb=xlrd.open_workbook('D:\下载\会员日优惠券使用范围.xlsx')
wb=openpyxl.load_workbook('会员日优惠券使用范围.xlsx')
xr=openpyxl.Workbook()
xsheet=xr.active
sheet=wb.active
# a=sheet.rows
# print(a)
# lst=[] #存取所有车站的名称及编号
for row in sheet.rows: # 遍历所有的行
    sub_list=[]
    for cell in row: # 遍历每一行中的单元格，每一行的结果放到sub_list中，再将sub_list添加到lst中
        sub_list.append(cell.value)
        xsheet.append(sub_list)
xr.save('D:\杂\x.xlsx')
        # print(cell.value)
    # print(sub_list)
#     lst.append(sub_list)
# print(dict(lst)) #将列表转换成字典，后期根据字典的键查找值（即：根据车站名字查找代号）