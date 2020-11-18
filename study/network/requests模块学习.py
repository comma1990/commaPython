# author : comma
# date : 2020/11/16 14:34

'''
requests模块、
常用方法：
    requests.get() ： 发送get请求
    requests.post() ： 发送post请求
    requests.head() ： 获取HTML的头部信息
    requests.put() ： 发送put请求
    requests.patch() ：提交局部修改请求
    requests.delete() ：提交删除请求

response对象的常用属性：
    response.status_code : 响应状态码
    response.content :把response对象转换为二进制数据
    response.text : 吧response对象转换成字符串数据
    response.encoding : 定义response对象的编码
    response.cookies : 获取请求后的cookie
    response.url : 获取请求网址
    response.json() :内置的json解码器
    Response.headers ：以字典对象存储服务器响应头，字典键不区分大小写
'''
import requests
import urllib3
import lxml
urllib3.disable_warnings()

# url = 'http://www.baidu.com'
# resp = requests.get(url)
# # 设置响应的编码格式
# resp.encoding = 'utf-8'
# cookie = resp.cookies
# headers = resp.headers
# print('响应状态码：', resp.status_code)
# print('请求后的cookie：', cookie)
# print('获取请求的网址', resp.url)
# print('响应头：', headers)
# print('响应内容：', resp.text)

################ get()带参数请求 ##########################
# url1='https://www.so.com/s'
# params={'q':'python'}
# resp1=requests.get(url1,params=params,verify=False)
# resp1.encoding='utf-8'
# print(resp1.text)

############# 下载图片,保存到本地 #########################
# url2='http://pic1.shop2cn.com/G03/M00/39/55/CgzUIF-L0bqAa4YlAANMTEa_HtE066_1_1_n_x_o.png'
# resp2=requests.get(url2)
#
# with open('D:\素材\轩尼诗.png','wb') as file:
#     file.write(resp2.content)

########### session请求 ########################################
url3 = 'https://www.shop2cn.com/service/shop/api/accountlogin'
headers = {'Accept': 'application/json, text/plain, */*',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
           }
requestData = {"username": "18862396927",
               "password": "q41ZxiimH+QTNSkdwYc1ybbNMo7c/vbuU+L2iRhEtTe1C+MyWk6XfDkCuPgj5JgoTIB4Cxmn/G2ECfbRyuxFN9mLllnUr0P7Lj2m4otCxyJ6ElGQx4vtQl+Uqb44zwP5wz6Ng7PUFFBEtDVyGvo6t3N4lTuWH/NN4C6xYKWsoNE="
               }

session=requests.session()
resp3=session.post(url3,json=requestData,headers=headers,verify=False)
resp3.encoding='utf-8'
print(resp3.text)
# 登录后的第二个请求，直接用session调用
url4='https://www.shop2cn.com/service/order/api/depot/getDepotList'
data = {"pageIndex": 1, "pageSize": 100}
resp4=session.post(url4,data=data)
resp4.encoding='utf-8'
print(resp4.text)

######################################################################