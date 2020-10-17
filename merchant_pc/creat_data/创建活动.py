# Author ： comma
# 日期 : 2020/10/17  10:14

# 创建活动
import requests
import urllib3
import json
import openpyxl
import xlrd

if __name__ == '__main__':
    wk = openpyxl.Workbook()
    sheet = wk.create_sheet()
    sheet.append(['productId', 'category'])

    from merchant_pc.getProductList import getPorductList
    for i in range(5):  # 循环5页的数据（getPorductList接口每次只返回20条数据）
        plist = getPorductList(1)
        for item in plist:
            # 此处应该加个判断，如果商品有活动id，调用活动判断的方法，如果有活动执行下面代码块，如果没有打印商品不符合
            from merchant_pc.ProductInfo import ProductInfo.get
            productid = item['id']
            categrorys = item['catalogList']
            for cat in categrorys:
                categrory = cat
                sheet.append([productid, str(categrory)])
                # print(productid,categrory)
    wk.save('/Users/sun/PycharmProjects/活动商品.xlsx')
