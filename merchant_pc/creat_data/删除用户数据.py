#-*- coding:utf-8 -*-
# author : comma
# date : 2020/11/12 9:57
'''
    1.统计昵称为'hahaha'的用户UserId的数量
    SELECT UserId ,COUNT(1) FROM `member` WHERE NickName='hahaha' GROUP BY UserId
'''
import os
import getCookie
import requests


def delete(userid):
    Cookie = getCookie.getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    requestData = {
        "userId": userid,
        "userType": 0,
        "nickName": "伊蓝"
    }
    url='http://dguser.iapi.ymatou.com/user/deleteUserSelf'
    data=requests.post(url=url,json=requestData,headers=headers,verify=False)
    print(data.text)


if __name__ == '__main__':
    with open('D:/python/UserID.txt', 'r', encoding='UTF-8') as userid:
        data = userid.readlines()
        for item in data:
            print(eval(item))
            delete(str(item))