# @Author  :  comma 
# @Date    :  2020-11-22 12:05


import requests
from bs4 import BeautifulSoup
import openpyxl


def send_request():
    url = 'https://www.xiachufang.com/explore/'
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
               }
    resp = requests.get(url, headers=headers)
    return resp.text


def parse_html(html):
    count = 0
    bs = BeautifulSoup(html, 'lxml')
    lst_name = bs.find_all('p', class_='name')
    lst_category = bs.find_all('p', class_="ing ellipsis")
    lst = []
    for i in range(len(lst_name)):
        count += 1
        food_url = 'https://www.xiachufang.com' + lst_name[i].find('a')['href']
        lst.append([count, lst_name[i].text[18:-15], lst_category[i].text[1:-1], food_url])
        # print(food_url)
    # print(lst)
    return lst

    # print(lst_name)


def save(lst):
    wb = openpyxl.Workbook()
    sheet = wb.active
    for row in lst:
        sheet.append(row)
    wb.save('下厨房案例.xlsx')


def start():
    result = send_request()
    lst=parse_html(result)
    save(lst)

if __name__ == '__main__':
    start()
