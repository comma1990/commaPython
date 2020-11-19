# @Author  :  comma 
# @Date    :  2020-11-19 21:59


import requests
import re

url='https://www.qiushibaike.com/video/'
headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
resp=requests.get(url,headers=headers)

info=re.findall('<source src="(.*)" type=\'video/mp4\'/>',resp.text)

lst=[]
for item in info:
    lst.append('https:'+item)

count=0
for item in lst:
    count+=1
    resp=requests.get(item,headers=headers)
    with open(f'/Users/sun/PycharmProjects/data/{count}.mp4','wb') as file:
        file.write(resp.content)