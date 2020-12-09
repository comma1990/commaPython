# @Author  :  comma 
# @Date    :  2020-12-07 22:50


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待方法
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Chrome()  # 创建浏览器对象


class TrainSpider():
    login_url = 'https://kyfw.12306.cn/otn/resources/login.html'  # 登录页面
    mycenter_url = 'https://kyfw.12306.cn/otn/view/index.html'  # 个人中心页面
    letf_ticket = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'  # 余票查询页面

    # 定义初始化方法
    def __init__(self, from_station, to_station, train_date, trains):
        self.from_station = from_station
        self.to_station = to_station
        self.train_date = train_date
        self.station_code = self.init_station_code()  # self.station_code结果是一个字典
        self.trains = trains

    def login(self):
        driver.get(self.login_url)
        WebDriverWait(driver, 1000).until(
            ec.url_to_be(self.mycenter_url)  # 等待直到url变成个人中心的页面
        )
        print('登录成功')

    def search_ticket(self):
        # 打开查询余票的网址
        driver.get(self.letf_ticket)

        # 找到出发站和到达站的隐藏标签
        fromStation_input = driver.find_element_by_id('fromStation')
        toStation_input = driver.find_element_by_id('toStation')
        train_date_input = driver.find_element_by_id('train_date')  # 找到出发时间的input标签

        # 根据键获取值
        fromStation_code = self.station_code.get(self.from_station)  # from_station为初始化方法传入的值，根据这个值获取车站对应的编号
        toStation_code = self.station_code.get(self.to_station)  # 根据目的地车站名称找到对应车站的编号

        # 执行js代码
        driver.execute_script('arguments[0].value="%s"' % fromStation_code,
                              fromStation_input)  # 将fromStation_code的值传入到fromStation_input标签中
        driver.execute_script('arguments[0].value="%s"' % toStation_code, toStation_input)
        driver.execute_script('arguments[0].value="%s"' % self.train_date, train_date_input)

        # 单击查询按钮，执行查询操作
        driver.find_element_by_id('query_ticket').click()

        # 等待页面加载出车次信息
        WebDriverWait(driver, 1000).until(
            ec.presence_of_all_elements_located((By.XPATH, '//tbody[@id="queryLeftTable"]/tr'))  # 通过xpath定位元素是否出现
        )
        # 筛选出有数据的tr，去掉属性为datatran的tr,通过xpath的not方法[not(@datatran)]
        trains = driver.find_elements_by_xpath('//tbody[@id="queryLeftTable"]/tr[not(@datatran)]')
        for train in trains:  # 遍历车次信息
            info = train.text.replace('\n', ' ').split(' ')  # 获取单个车次的信息，并放到列表中
            train_no = info[0]  # 列表中索引为0的为车次
            if train_no in self.trains:  # 这里的self.trains是初始化方法用户传入的车次
                # 根据key获取值，席别是一个列表
                seat_types = self.trains[train_no]
                for seat_type in seat_types:  # 遍历席位列表
                    if seat_type == 'O':  # 说明是二等座
                        count=info[9]
                        if count.isdigit() or count=='有': #isdigit()判断字符串是否为数字
                            #有票后点击预定按钮
                            order_btn=train.find_element_by_xpath('.//a[@class="btn72"]')
                            order_btn.click()
                    if seat_type == 'M':  # 说明是一等座
                        pass

            # print(info.text)

    # 负责调用其他方法(组织其他的代码)
    def run(self):
        # 1.登录
        self.login()
        # 2.余票查询
        self.search_ticket()

    def init_station_code(self):  # 初始化车站编号（从Excel表中读取）
        wb = openpyxl.load_workbook('车站编号.xlsx')
        sheet = wb.active
        lst = []  # 存取所有车站的名称及编号
        for row in sheet.rows:  # 遍历所有的行
            sub_list = []
            for cell in row:  # 遍历每一行中的单元格，每一行的结果放到sub_list中，再将sub_list添加到lst中
                sub_list.append(cell.value)
            lst.append(sub_list)
        # print(dict(lst))  # 将列表转换成字典，后期根据字典的键查找值（即：根据车站名字查找代号）
        return dict(lst)


def start():
    spider = TrainSpider('上海', '连云港', '2020-12-15', {'d782': ['o', 'M']})  # o表示的是二等座，M表示一等座
    spider.run()
    spider.init_station_code()


if __name__ == '__main__':
    start()
