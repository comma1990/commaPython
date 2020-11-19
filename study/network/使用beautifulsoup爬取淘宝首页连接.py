#author : comma
#date : 2020/11/19 13:55

############### 爬取淘宝网首页的链接 ##################
import urllib3
import requests
from bs4 import BeautifulSoup


urllib3.disable_warnings()
url='http://www.taobao.com'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
resp=requests.get(url,headers=headers,verify=False)
#print(resp.text)
bs=BeautifulSoup(resp.text,'lxml')
a_list=bs.find_all('a')
# print(len(a_list))
for a in a_list:
    url=a.get('href')
    if url==None:
        continue
    if url.startswith('http'):
        print(url)