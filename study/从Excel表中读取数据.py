#author : comma
#date : 2020/10/16 14:58

# 从Excel表中读取数据
import xlrd

wk=xlrd.open_workbook('D:\python\study\商品图片地址.xlsx')
sheet=wk.sheets()[0]    # 获取索引为0的表
#print(sheet.col_values(0,1,3))  # 获取sheet表，第0列，第1到第3行数据（0，1,3都是索引）
#print(sheet.row_values(0,0,3))  # 获取sheet表，第0行，第1到第3列数据
#print(sheet.col_values(0)) # 获取第一列的q全部数据
i=0
for item in range(sheet.nrows): #sheet.nrows 获取表的行数；sheet.ncols获取表的列数
    print(sheet.col_values(0,i,i+1))
    i+=1
#print(coldata)