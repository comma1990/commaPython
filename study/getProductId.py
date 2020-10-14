# Author ： comma
# 日期 : 2020/10/14  23:48
import xlrd

wk = xlrd.open_workbook('/Users/sun/PycharmProjects/商品信息.xlsx') #读取目录位置文件
data = wk.sheets()[1] #[1]表示索引为1的表
#【读取列数据】循环读去第0列的第i到第i+3行数据
for i in range(5):
    if i !=0:
        productIdList = data.col_values(0, i, i + 3) #读去第0列，第i行到第i+3行数据
        i += 3
        s=str(productIdList).replace("'","\"")
        print(s)

# 读取行数据
# x=data.row_values(0,1,4) #读去第0行，第1到第4列数据，如果要读去一整行数据只保留0就可以了
# print(x)
# createCoupon()