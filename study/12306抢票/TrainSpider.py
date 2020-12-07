# @Author  :  comma 
# @Date    :  2020-12-07 22:50


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # 显示等待方法
from selenium.webdriver.support import expected_conditions as ec


driver=webdriver.Chrome()#创建浏览器对象


class TrainSpider():
    login_url='https://kyfw.12306.cn/otn/resources/login.html'
    mycenter_url='https://kyfw.12306.cn/otn/view/index.html'
    # 定义初始化方法
    def __init__(self,from_station,to_station,train_date):
        self.from_station=from_station
        self.to_station=to_station


    def login(self):
        driver.get(self.login_url)
        WebDriverWait(driver,1000).until(
            ec.url_to_be(self.mycenter_url) # 等待直到url变成个人中心的页面
        )
        print('登录成功')




    # 负责调用其他方法(组织其他的代码)
    def run(self):
        self.login()

if __name__ == '__main__':
    spider=TrainSpider('连云港','上海','2020-12-10')
    spider.run()