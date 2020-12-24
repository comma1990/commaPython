# @Author  :  comma 
# @Date    :  2020-12-06 18:21


'''
行为链如何使用：
    导入from selenium_test.webdriver.comma.action_chains import ActionChains
    创建对象actions=ActionChains(driver)
    移动到某元素 actions.move_to_element(element)
    文本框填入内容 actions.send_keys_to_element(element,'python')
    单击 actions.click(element)
    双击 double_click(element)
    右键点击 context_click(element)
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 导入selenium行为链
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time


def my_actions(): # 行为链
    global driver
    # 构造浏览器
    driver = webdriver.Chrome()
    driver.get('https://cn.bing.com/')
    search_input = driver.find_element_by_id('sb_form_q')  # 获取搜索输入框
    search_button = driver.find_element_by_id('sb_form_go')  # 获取搜索按钮

    # 创建行为链
    acitons = ActionChains(driver)
    acitons.move_to_element(search_input)  # 移动到搜索输入框上
    acitons.send_keys_to_element(search_input, 'python')  # 输入python
    acitons.move_to_element(search_button)  # 移动到搜索按钮上
    acitons.click(search_button)  # 点击搜索按钮

    # 开始执行行为链
    acitons.perform()

    time.sleep(5)
    driver.quit()


def use_cookie(): # cookie操作
    # 构造浏览器
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')

    # 获取所有的cookie信息
    cookies = driver.get_cookies()
    for cookie in cookies:
        print(cookie)
    print('-----------------------')
    # 获取指定的cookie信息
    cookie=driver.get_cookie('BD_HOME') # 这里只能根据name的值来获取
    print(cookie)

    # 添加cookie
    driver.add_cookie({'name':'test','value':'comma'})
    print(driver.get_cookie('test'))

    # s删除cookie
    driver.delete_cookie('test')
    print(driver.get_cookie('test'))
    print('-----------------------------------------------------')

    # 删除所有的cookie
    driver.delete_all_cookies()
    print(driver.get_cookies())


def page_wait():# 页面等待
    '''
    隐式等待：
        调用driver.implicitly_wait 那么在获取不可用的元素之前，会先等等N秒钟的时间
    显示等待：
        显示等待是表明某个条件成立后才执行获取元素的操作，也可以在等待的时候指定一个最大的时间，如果超过这个时间就会抛出一个异常
    '''
    # driver=webdriver.Chrome()
    # driver.get('https://www.baidu.com')

    # #隐式等待
    # driver.implicitly_wait(5) # 等待5秒
    # driver.find_element_by_id('hhhhh') # 乱写的值，会报错

    # 显示等待
    global driver2
    driver2=webdriver.Chrome()
    driver2.get('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc')
    WebDriverWait(driver2,100).until(ec.text_to_be_present_in_element_value((By.ID,'fromStationText'),'上海'))
    WebDriverWait(driver2,100).until(ec.text_to_be_present_in_element_value((By.ID,'toStationText'),'连云港'))

    query_button=driver2.find_element_by_id('query_ticket')
    query_button.click()


if __name__ == '__main__':
    # my_actions()
    # use_cookie()
    page_wait()