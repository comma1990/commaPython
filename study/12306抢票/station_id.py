# @Author  :  comma 
# @Date    :  2020-12-07 23:07


import requests
import re
import openpyxl


def get_station():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9169'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    responsedata = requests.get(url, headers=headers)
    responsedata.encoding = 'utf-8'
    # print(responsedata.text)

    stations = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)', responsedata.text)
    # print(stations)
    return stations

def save(lst):
    wb = openpyxl.Workbook()
    sheet = wb.active
    for item in lst:
        sheet.append(item)
    wb.save('/Users/sun/PycharmProjects/commaPython/study/12306抢票/车站编号.xlsx')


if __name__ == '__main__':
    lst = get_station()
    save(lst)
