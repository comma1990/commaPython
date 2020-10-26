# Author ： comma
# 日期 : 2020/10/16  23:42

# 获取++创建活动时++拉取的商品列表
import requests
import urllib3
import json
import openpyxl

def getPorduceList(Cookie,pageIndex): # pageIndex页码，你想获得哪页的数据
    # from merchant_pc.getCookie import getCookies  # cookie获取提取到方法外，调用该方法必须穿cookie
    # Cookie = getCookies()
    #text/html,application/xhtml+xml,application/xml
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng, */*',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    '''设置请求数据'''
    #json=requestData,?status=1&pageIndex=1&pageSize=20
    #requestData = {"status": 1,"pageIndex":int(pageIndex), "pageSize": 100},json=requestData,
    urllib3.disable_warnings()
    data = requests.get(f'https://www.shop2cn.com/service/mgmt/api/page/produceList?status=1&pageIndex={pageIndex}&pageSize=20',
                         headers=headers,
                         verify=False)
    response = data.text
    productList=json.loads(response)['data']['productList']
    #print(productList)
    return productList

if __name__ == '__main__':
    wk=openpyxl.Workbook()
    sheet=wk.create_sheet('活动商品列表')
    x=0     # 计数器
    sellerid=eval(input('请输入商户id：'))
    n=int(input('请输入你想添加的商品个数：'))
    #discount = 5.6  # 设置折扣
    discount=int(input('请输入折扣：'))
    # 遍历商品列表，并在商品规格上添加活动库存信息
    for item in getPorduceList(1):   #遍历商品列表
        productid=[item['id']]
        from merchant_pc.getPoductActivityInfo import getPoductActivityInfo
        if bool(getPoductActivityInfo(sellerid,productid))==False:     #判断商品没有活动信息后，添加规格的活动信息，并添加到Excel表中
            for catlog in item['catalogList']:  #遍历规格列表
                catlog['activityRealStock']=0    #添加活动真实库存
                catlog['activityStock']=0    # 添加活动库存 ——为0的时候默认使用全部库存
                catlog['discount']=discount     # 添加折扣信息
                catlog['discountPrice']=catlog['salePrice']*discount/10   # 添加折后价格
                sheet.append([item['id'], str(catlog).replace('\'', '"')])
                x+=1
                if x>n:
                    break

    wk.save('D:\python\study\活动商品列表.xlsx')
        #print(catlog)
    #getPorduceList(2)