import random
import urllib3
import requests


# '''创建客服专员'''
def create_kefuzhuanyuan(Cookie):
    # from merchant_pc.getCookie import getCookies
    # Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    '''创建客服专员'''
    x = random.randint(10, 50)
    loginId = 'kfzy' + str(x)
    title = '客服专员' + str(x)
    requestData = {"templateId": 304,
                   "loginId": loginId,
                   "title": title,
                   "password": "sun12345"}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/order/api/cservice/addCS', json=requestData, headers=headers,
                         verify=False)
    response = data.text
    print(response)


#   '''创建邀请客服'''
def create_yaoqingkefu(Cookie):
    # from merchant_pc.getCookie import getCookies
    # Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    x = random.randint(10, 50)
    loginId = 'yqkf' + str(x)
    title = '邀请客服' + str(x)
    requestData = {"templateId": 11,
                   "loginId": loginId,
                   "title": title,
                   "password": "sun12345"}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/order/api/cservice/addCS', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    print(response)


# '''创建高级管理员'''
def create_gaojiguanliyuan(Cookie):
    # from merchant_pc.getCookie import getCookies
    # Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    x = random.randint(10, 50)
    loginId = 'gjgly' + str(x)
    title = '高级管理员' + str(x)
    '''设置角色id——templateId'''
    requestData = {"templateId": 301,
                   "loginId": loginId,
                   "title": title,
                   "password": "sun12345"}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/order/api/cservice/addCS', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    print(response)


# '''创建普通管理员'''
def create_putongguanliyuan(Cookie):
    # from merchant_pc.getCookie import getCookies
    # Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    x = random.randint(10, 50)
    loginId = 'ptgly' + str(x)
    title = '普通管理员' + str(x)
    '''设置角色id——templateId'''
    requestData = {"templateId": 302,
                   "loginId": loginId,
                   "title": title,
                   "password": "sun12345"}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/order/api/cservice/addCS', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    print(response)


# '''创建客服主管'''
def create_kefuzhuguan(Cookie):
    # from merchant_pc.getCookie import getCookies
    # Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    x = random.randint(10, 50)
    loginId = 'kfzg' + str(x)
    title = '客服主管' + str(x)
    '''设置角色id——templateId'''
    requestData = {"templateId": 303,
                   "loginId": loginId,
                   "title": title,
                   "password": "sun12345"}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/order/api/cservice/addCS', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    print(response)


# '''创建发货和仓库管理员'''
def create_fahuohecangkuguanliyuan(Cookie):
    # from merchant_pc.getCookie import getCookies
    # Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    x = random.randint(10, 50)
    loginId = 'fhcg' + str(x)
    title = '发货和仓库管理员' + str(x)
    '''设置角色id——templateId'''
    requestData = {"templateId": 305,
                   "loginId": loginId,
                   "title": title,
                   "password": "sun12345"}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/order/api/cservice/addCS', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    print(response)


# '''创建销售专员'''
def create_xiaoshouzhuanyuan(Cookie):
    # from merchant_pc.getCookie import getCookies
    # Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    x = random.randint(10, 50)
    loginId = 'xszy' + str(x)
    title = '销售专员' + str(x)
    '''设置角色id——templateId'''
    requestData = {"templateId": 306,
                   "loginId": loginId,
                   "title": title,
                   "password": "sun12345"}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/order/api/cservice/addCS', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    print(response)


# '''创建商品管理员'''
def create_shangpingguanliyuan(Cookie):
    # from merchant_pc.getCookie import getCookies
    # Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    x = random.randint(10, 50)
    loginId = 'spgly' + str(x)
    title = '商品管理员' + str(x)
    '''设置角色id——templateId'''
    requestData = {"templateId": 307,
                   "loginId": loginId,
                   "title": title,
                   "password": "sun12345"}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/order/api/cservice/addCS', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    print(response)


# '''创建财务'''
def create_caiwu(Cookie):
    # from merchant_pc.getCookie import getCookies
    # Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    x = random.randint(10, 50)
    loginId = 'cw' + str(x)
    title = '财务' + str(x)
    '''设置角色id——templateId'''
    requestData = {"templateId": 308,
                   "loginId": loginId,
                   "title": title,
                   "password": "sun12345"}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/order/api/cservice/addCS', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    print(response)


# '''创建美工'''
def create_meigong(Cookie):
    # from merchant_pc.getCookie import getCookies
    # Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    x = random.randint(10, 50)
    loginId = 'mg' + str(x)
    title = '美工' + str(x)
    '''设置角色id——templateId'''
    requestData = {"templateId": 309,
                   "loginId": loginId,
                   "title": title,
                   "password": "sun12345"}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/order/api/cservice/addCS', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    print(response)


# '''创建直播专员'''
def create_zhibozhuanyuan(Cookie):
    # from merchant_pc.getCookie import getCookies
    # Cookie = getCookies()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com',
               'Connection': 'keep - alive',
               'Cookie': Cookie
               }
    x = random.randint(10, 50)
    loginId = 'zbzy' + str(x)
    title = '直播专员' + str(x)
    '''设置角色id——templateId'''
    requestData = {"templateId": 310,
                   "loginId": loginId,
                   "title": title,
                   "password": "sun12345"}
    urllib3.disable_warnings()
    data = requests.post('https://www.shop2cn.com/service/order/api/cservice/addCS', json=requestData,
                         headers=headers,
                         verify=False)
    response = data.text
    print(response)
