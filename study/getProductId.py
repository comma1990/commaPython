# Author ： comma
# 日期 : 2020/10/14  23:48
import xlrd

wk = xlrd.open_workbook('/Users/sun/PycharmProjects/商品信息.xlsx')  # 读取目录位置文件
data = wk.sheets()[1]  # [1]表示索引为1的表

n = int(input('请输入你想创建活动的商品数量：'))
i = 0
# 【读取列数据】循环读去第0列的第i到第i+3行数据


actProIdList = []
for item in range(1, data.nrows):  # 从1开始遍历
    actProId = data.col_values(0, item, item + 1)  # 读去第0列，第i行到第i+1行数据

    from merchant_pc.getPoductActivityInfo import getPoductActivityInfo
    if True:
    #if (getPoductActivityInfo(actProId)) != None:
        while i < n:    # 根据输入的数量，循环多少次
            actProIdList.append(actProId)
            i += 1
print(actProIdList)

# 读取行数据
# x=data.row_values(0,1,4) #读去第0行，第1到第4列数据，如果要读去一整行数据只保留0就可以了
# print(x)
# createCoupon()
