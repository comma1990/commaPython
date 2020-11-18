# @Author  :  comma 
# @Date    :  2020-11-14 16:44


'''
urllib是python自带的标准库中用于网络请求的库，无需安装，直接引用即可。
    通常用于爬虫开发，API（应用程序编程接口）数据获取和测试

urllib库的4大模块：
    urllib.request:用于打开和读取URL
    urllib.error:包含提出的例外（异常）urllib.request
    urllib.parse:用于解析URL
    urllib.robotparser:用于解析robots.txt文件

urllib.request.urlopen语法格式:
    urlopen(url,data=None,[timeout,]*,cafile=None,capath=None,cadefault=False.context=None)
        参数说明：url参数是str类型，如：'https://www.baidu.com'
                data:默认值为None，urllib判断data为空时使用get请求，不为空时使用post请求。data以字典形式存储，使用时要转换成字节类型才能完成post请求
'''
import ssl
import urllib.parse
import urllib.request

ssl._create_default_https_context=ssl._create_unverified_context
import urllib3.request

kw = {'wd': '逗号'}
# 编码
result = urllib.parse.urlencode(kw)
print(result)
# 解码
print(urllib.parse.unquote(result))

# print('--------------------------------')


################ urllib.request.urlopen使用方法演示 ####################
# url = 'https://www.xslou.com/login.php'
# data = {'username': '18862396927', 'password': '57635763', 'action': 'login'}
# response = urllib.request.urlopen(url, data=bytes(urllib.parse.urlencode(data), encoding='utf-8'))
# rslt = response.read().decode('gbk')
# print(rslt)

############## 需要添加请求头时处理方式 #################3
# url1 = 'https://movie.douban.com/'
# headers = {'Accept': 'application/json, text/plain, */*',
#            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
#            }
# # 构建请求对象
# request=urllib.request.Request(url1,headers=headers)
# resp=urllib.request.urlopen(request)
# rest=resp.read().decode('utf-8')
# print(rest)

############## 设置访问代理 ##################
# from urllib.request import build_opener
# from urllib.request import ProxyHandler
# proxy=ProxyHandler({'https':'121.226.188.19:9999'}) # 设置访问代理
# opener=build_opener(proxy)  # urlopen是重写了build_opener方法，这里我们自己直接调用build_opener方法
# url='https://www.xslwx.com/'
# rep=opener.open(url)
# print(rep.read().decode('utf-8'))