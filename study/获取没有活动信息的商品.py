# Author ： comma
# 日期 : 2020/10/18  19:55

# from merchant_pc.ProductInfo import getPoductActivityInfo

#  cell = sheet.cell(row=1,column=1) 获取某一行某一列的数据
import xlrd

wk = xlrd.open_workbook('/Users/sun/PycharmProjects/商品信息.xlsx')  # 读取目录位置文件
data = wk.sheets()[1]  # [1]表示索引为1的表
n = int(input('请输入你想创建活动的商品数量：'))
i = 0
list = []
actProIdList = []
for item in range(1, data.nrows):
    #productId = data.col_values(0, item, item + 1)  # 读去第0列，第i行到第i+1行数据 ！！！！！这种方式取到的值是列表！！！！
    productId=data.cell_value(item,0)   # sheet.cell_value(rowx,colx) 获取第几行第几列的数据放到括号里替代就好了
    list.append(productId)
for x in list:
    if x != 'p5985277':
        #print(x)
        actProIdList.append(x)
        i+=1
        if i==n:
            break
print(actProIdList)

