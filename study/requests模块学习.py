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

url = 'http://www.baidu.com'
resp = requests.get(url)
# 设置响应的编码格式
resp.encoding = 'utf-8'
cookie = resp.cookies
headers = resp.headers
print('响应状态码：', resp.status_code)
print('请求后的cookie：', cookie)
print('获取请求的网址', resp.url)
print('响应头：', headers)
print('响应内容：', resp.text)
