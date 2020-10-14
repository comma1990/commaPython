import requests
import urllib3

def getCookies():
    urllib3.disable_warnings()
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': 'www.shop2cn.com'}
    requestData = {"username": "18862396927",
                   "password": "aLhnKT0fG+oQRwX2MG0HLeDB9DG2iYSes8VR4w36oPaSJYVfgFXxePzr0tlKfkXjildB2wIrDdDAZC/MBkr4IJ4zW2iacwAdN6Srv+UjtTKuRI6GzjRuf0WmHYUS/QcFD+4OJqOrQYkxWsR5awgDgCt9TyLQPHz0Bk84cwghuZA="}
    data = requests.post('https://www.shop2cn.com/service/shop/api/accountlogin',
                         json=requestData,
                         headers=headers,
                         verify=False)
    cookies = data.cookies.items()
    cookie = ''
    for name, value in cookies:
        cookie += '{0}={1};'.format(name, value)
    #print(data)
    return cookie
