import requests
import urllib3

'''
{"username":"16011112222","password":"kSe/n6c23Zai4PbiB1+ISQhXO9WGqU3AeMqqscH+Ce3k/PyNlMx6zrKhaPSvUzWbtSdfx9zFl3Btx5H2cKpWVhj/nymmQfp4LFhFPXa5rHBKOPVRg1t2VUzWz42AGAUasgJ7hlAqOHIL/iJWvYfMsDzApLv83bqhbiBg20iCZos="}
{"username":"14600001111","password":"NrYo3OdUar4MLC/r8MVgf/MawXukdiQJFB/asrl0flDreSSyzeu4w2qoxmSqU7yUR3Xl/d9kyTf19f0S2ZIkCUrv9llpKfNrXXqCYBjzwrJ4GspwEULha3P2WMXfrX9RR+zWMfle7Hvpk81fTnbyNSANfKIXhu7I7VEe4m54DDg="}
{"username":"150123456","password":"MWoFtxdJlLwJwP4A/uKc419H7IqdtB6sFGGTQphrdhPWXoRu0S60/I+Fm+gNeBdLoVGt3q2cQB6NiG3NFUsfdJf9b9+0j4LRrDKr5vUTfndpgYT6i0x8opeorZSoSK2Uww9uCThFkVnQXlYIzK/sAYlmdAgJfeRGHJCjeSwJMFw="}
'''


def getCookies():
    urllib3.disable_warnings()
    url = 'https://www.shop2cn.com/service/shop/api/accountlogin'  # 公版登录地址
    # url='https://www.crossbiz.shop/service/shop/api/accountlogin' # 洋货街测试
    requestData = {"username": "18862396927",
                   "password": "q41ZxiimH+QTNSkdwYc1ybbNMo7c/vbuU+L2iRhEtTe1C+MyWk6XfDkCuPgj5JgoTIB4Cxmn/G2ECfbRyuxFN9mLllnUr0P7Lj2m4otCxyJ6ElGQx4vtQl+Uqb44zwP5wz6Ng7PUFFBEtDVyGvo6t3N4lTuWH/NN4C6xYKWsoNE="}
    #requestData={"username":"17711112223","password":"Y3U2yJ540qRl42i6Z5rP1V1KE0wfrQ1f0puqEvXqmnhHqASEWQ3bWPwpfhC8dsbCF6gPRn45qPprVIAUrwnngkitQDhJ5rYHtjdWvGVeHRXyrOT24nniFQFFoN0pWuNroOtvY/xHUYO9Chq1TCACcdRtPRSYHNWiVXTRE71k4Ys="}
    # requestData={"username":"16400001111","password":"kSe/n6c23Zai4PbiB1+ISQhXO9WGqU3AeMqqscH+Ce3k/PyNlMx6zrKhaPSvUzWbtSdfx9zFl3Btx5H2cKpWVhj/nymmQfp4LFhFPXa5rHBKOPVRg1t2VUzWz42AGAUasgJ7hlAqOHIL/iJWvYfMsDzApLv83bqhbiBg20iCZos="}
    # requestData={"username":"121131","password":"GdKWG4p1jHW9k6Y9T7rrfBXwXB33ej2TUP+Ezxj0LDG3E+oJ85LnSyPkpgM+0daZR6xwmJdXsI+9hEvRpcF2J9h3uYvHfbx4Ww5gPE+XJ8xEpKehxhkKgRbyF3VqGcr+oJl678OvwEfvbYs7ZTqY7XCGHnoraP22Ev0sug+ixOg=","wxAppName":"pcsqSeller_500011795"}


    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

    data = requests.post(url, json=requestData, headers=headers, verify=False)
    cookies = data.cookies.items()
    cookie = ''
    for name, value in cookies:
        cookie += '{0}={1};'.format(name, value)
    print(cookie)
    return cookie


if __name__ == '__main__':
    getCookies()
