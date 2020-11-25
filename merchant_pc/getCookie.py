import requests
import urllib3
'''
{"username":"16011112222","password":"kSe/n6c23Zai4PbiB1+ISQhXO9WGqU3AeMqqscH+Ce3k/PyNlMx6zrKhaPSvUzWbtSdfx9zFl3Btx5H2cKpWVhj/nymmQfp4LFhFPXa5rHBKOPVRg1t2VUzWz42AGAUasgJ7hlAqOHIL/iJWvYfMsDzApLv83bqhbiBg20iCZos="}
{"username":"14600001111","password":"NrYo3OdUar4MLC/r8MVgf/MawXukdiQJFB/asrl0flDreSSyzeu4w2qoxmSqU7yUR3Xl/d9kyTf19f0S2ZIkCUrv9llpKfNrXXqCYBjzwrJ4GspwEULha3P2WMXfrX9RR+zWMfle7Hvpk81fTnbyNSANfKIXhu7I7VEe4m54DDg="}
'''

def getCookies():
    urllib3.disable_warnings()
    host = 'www.shop2cn.com'
    url = 'https://www.shop2cn.com/service/shop/api/accountlogin'  # 公版登录地址
    requestData = {"username": "18862396927",
                   "password": "q41ZxiimH+QTNSkdwYc1ybbNMo7c/vbuU+L2iRhEtTe1C+MyWk6XfDkCuPgj5JgoTIB4Cxmn/G2ECfbRyuxFN9mLllnUr0P7Lj2m4otCxyJ6ElGQx4vtQl+Uqb44zwP5wz6Ng7PUFFBEtDVyGvo6t3N4lTuWH/NN4C6xYKWsoNE="}

    # requestData={"username":"16011112222","password":"kSe/n6c23Zai4PbiB1+ISQhXO9WGqU3AeMqqscH+Ce3k/PyNlMx6zrKhaPSvUzWbtSdfx9zFl3Btx5H2cKpWVhj/nymmQfp4LFhFPXa5rHBKOPVRg1t2VUzWz42AGAUasgJ7hlAqOHIL/iJWvYfMsDzApLv83bqhbiBg20iCZos="}


    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': host}

    data = requests.post(url, json=requestData, headers=headers, verify=False)
    cookies = data.cookies.items()
    cookie = ''
    for name, value in cookies:
        cookie += '{0}={1};'.format(name, value)
    print(cookie)
    return cookie


if __name__ == '__main__':
    getCookies()
