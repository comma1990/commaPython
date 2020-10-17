import requests
import urllib3


def getCookies():
    urllib3.disable_warnings()
    host = 'www.shop2cn.com'
    url = 'https://www.shop2cn.com/service/shop/api/accountlogin'  # 公版登录地址
    requestData = {"username": "18862396927",
                   "password": "aLhnKT0fG+oQRwX2MG0HLeDB9DG2iYSes8VR4w36oPaSJYVfgFXxePzr0tlKfkXjildB2wIrDdDAZC/MBkr4IJ4zW2iacwAdN6Srv+UjtTKuRI6GzjRuf0WmHYUS/QcFD+4OJqOrQYkxWsR5awgDgCt9TyLQPHz0Bk84cwghuZA="}

    ###############这块是中免的请求参数###########################
        # host='shop.cdfmembers.com'    # 中免host
        # url = 'https://shop.cdfmembers.com/service/shop/api/accountlogin'  # 中免登录地址
        # requestData = {"username": "...wx...13510237024",
        #                "password": "ldsoyxyeCnktDi3HblKbuFrbpFVrjRpqnaR8c5Hpba9M5CzRqpG3Ex7Y+mcMveuAAMfayN2IMaUELY9FB5jCIcHsR6xUwyJUYxcCbs1Yjn+onr6P2HIcxLO1MHlv3d34ekMubCOBREnYPYOMsFlzKjE3w7HAewkzsYS6N1kmjng=",
        #                "wxAppName": "pcsqSeller_500024716"}
    ######################################################

    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': host}

    data = requests.post(url, json=requestData, headers=headers, verify=False)
    cookies = data.cookies.items()
    cookie = ''
    for name, value in cookies:
        cookie += '{0}={1};'.format(name, value)
    #print(cookie)
    return cookie


if __name__ == '__main__':
    getCookies()
