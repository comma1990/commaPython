# @Author  :  comma 
# @Date    :  2020-12-04 22:37

'''
selenium定位元素：
    find_element 获取满足条件的第一个元素
    find_elements 获取满足条件的所有元素
    方法:
        find_element_by_id() : 通过ID定位元素
        find_element_by_name(): 通过name定位元素
        find_element_by_class_name(): 通过类样式名称定位元素
        find_element_by_tag_name() : 通过标签名称定位元素
        find_element_by_link_text() : 通过链接定位元素
        find_element_by_css_selector() : 通过css定位元素
        find_element_by_xpath() : 通过xpath语法来定位元素

'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def demo():
    chrome = webdriver.Chrome()
    chrome.get('https://www.baidu.com')
    time.sleep(3)
    chrome.close()  # 关闭当前窗口
    chrome.quit()  # 退出浏览器


def element_id():  # 根据id定位元素
    chrome = webdriver.Chrome()
    chrome.get('https://www.2345.com/')
    search_input = chrome.find_element_by_id('schInput')  # 根据id定位元素
    search_input.send_keys('python')
    time.sleep(10)


def element_name():  # 通过name定位元素
    chrome = webdriver.Chrome()
    chrome.get('https://www.2345.com/')
    search_input = chrome.find_element_by_name('word')  # 通过name定位元素
    search_input.send_keys('菜鸟教程')
    time.sleep(5)


def element_class_name():  # 通过class名字定位元素
    chrome = webdriver.Chrome()
    chrome.get('https://www.2345.com/')
    search_input = chrome.find_element_by_class_name('sch_input')  # 通过class名字定位元素
    search_input.send_keys('京东')
    time.sleep(5)


def element_tag_name():  # 通过tag标签名字定位元素
    global chrome
    chrome = webdriver.Chrome()
    chrome.get('https://www.baidu.com/')
    search_input = chrome.find_element_by_tag_name('input')  # 通过tag标签名字定位元素，页面中相同标签名字很多，所以不容易准确定位
    print(search_input)
    # search_input.send_keys('淘宝')
    time.sleep(5)
    chrome.quit()


def element_link_text():  # 通过链接来定位元素
    global chrome
    chrome = webdriver.Chrome()
    chrome.get('https://www.baidu.com/')
    link_text = chrome.find_element_by_link_text('地图')  # 通过链接来定位元素
    link_text.click()
    chrome.quit()


def element_css_selector():  # 通过css样式来定位元素
    global chrome
    chrome = webdriver.Chrome()
    chrome.get('https://cn.bing.com/')  # sb_form_q
    # search_input=chrome.find_element_by_css_selector('#sb_form_q') # 通过css样式来定位元素，通过id定位时要加 #
    # search_input.send_keys('通过id定位要带#')
    search_input = chrome.find_element_by_css_selector('.b_searchbox')  # 通过css来定位元素，使用class定位时要加 .
    search_input.send_keys('通过class定位要带.')
    chrome.quit()


def element_xpath():  # 通过xpath定位搜索框
    global chrome
    chrome = webdriver.Chrome()
    chrome.get('https://cn.bing.com/')
    search_input = chrome.find_element_by_xpath('//input[@class="b_searchbox"]')  # 通过xpath定位搜索框
    search_input.send_keys('xpath定位')
    time.sleep(3)
    search_button = chrome.find_element_by_xpath('//div[@id="sb_go_par"]')  # 获取搜索按钮元素，点击
    search_button.click()
    chrome.quit()


def checkbox():  # 操作复选框
    global chrome
    chrome = webdriver.Chrome()
    chrome.get('https://mail.163.com/register/index.htm?from=163navi&regPage=163')  # 网易邮箱注册页面
    checkbox_tag = chrome.find_element_by_xpath('//div[@class="custom-checkbox service"]/span')
    checkbox_tag.click()
    chrome.quit()


def selectbox():  # 下拉列表框元素的选择
    '''
    示例：
     <select class="w200sel" id="cardType">
        <option value="0">中国居民身份证</option>
        <option value="C">港澳居民来往内地通行证</option>
        <option value="G">台湾居民来往大陆通行证</option>
        <option value="B">护照</option>
     </select>
    '''
    global chrome
    chrome = webdriver.Chrome()
    chrome.get('https://kyfw.12306.cn/otn/regist/init')
    select = Select(chrome.find_element_by_id('cardType'))  # 获取下拉列表框的定位后，放入Select中
    # select.select_by_index(1)   # 通过索引选择下拉列表中的选项
    # select.select_by_visible_text('台湾居民来往大陆通行证') # 通过可见文本选择下拉列表中的选项
    select.select_by_value('B')  # 通过value选择下拉列表中的选项
    time.sleep(5)
    chrome.quit()

def anli(): # 搜索'python'，并将结果打印
    chrome=webdriver.Chrome()
    chrome.get('https://cn.bing.com/')
    # 获取网页元素
    search_input=chrome.find_element_by_id('sb_form_q')
    search_input.send_keys('python')
    # 获取按钮
    submit_button=chrome.find_element_by_id('sb_go_par')
    submit_button.click()
    print(chrome.page_source)
    time.sleep(5)
    chrome.quit()


if __name__ == '__main__':
    # demo()
    # element_id()
    # element_name()
    # element_class_name()
    # element_tag_name()
    # element_link_text()
    # element_css_selector()
    # element_xpath()
    # checkbox()
    selectbox()
    # anli()