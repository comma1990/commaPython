# @Author  :  comma 
# @Date    :  2020-12-07 22:50

'''
多次使用
WebDriverWait方法，以及expected_conditions方法结合By方法定位元素
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待方法
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
import openpyxl

driver = webdriver.Chrome()  # 创建浏览器对象


class TrainSpider():
    login_url = 'https://kyfw.12306.cn/otn/resources/login.html'  # 登录页面
    mycenter_url = 'https://kyfw.12306.cn/otn/view/index.html'  # 个人中心页面
    letf_ticket = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'  # 余票查询页面
    confirm_url='https://kyfw.12306.cn/otn/confirmPassenger/initDc' # 确认乘车人和坐席

    # 定义初始化方法
    def __init__(self, from_station, to_station, train_date, trains,passenger_name_list):
        self.from_station = from_station
        self.to_station = to_station
        self.train_date = train_date
        self.station_code = self.init_station_code()  # self.station_code结果是一个字典
        self.trains = trains
        self.passenger_name_list=passenger_name_list
        self.selected_no=None # 选中的车次
        self.selected_seat=None # 最后确认的坐席

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
        is_flag=False # 用来标记是否有余票，没有余票为False，有余票为True
        while True:
            for train in trains:  # 遍历车次信息
                infos = train.text.replace('\n', ' ').split(' ')  # 获取单个车次的信息，并放到列表中
                print(
                    infos)  # ['G8262', '上海', '连云港', '09:08', '13:12', '04:04', '当日到达', '--', '10', '有', '--', '--', '--', '--', '--', '--', '无', '--', '预订']
                train_no = infos[0]  # 列表中索引为0的车次信息
                if train_no in self.trains:  # 这里的self.trains是初始化方法用户传入的车次
                    # 根据key获取值，席别是一个列表
                    seat_types = self.trains[train_no]
                    for seat_type in seat_types:  # 遍历席位列表
                        if seat_type == 'O':  # 说明是二等座
                            count = infos[9]
                            if count.isdigit() or count == '有':  # isdigit()判断字符串是否为数字
                                # 有票后点击预定按钮
                                is_flag = True
                                break  # 退出遍历席位的循环
                                # order_btn = train.find_element_by_xpath('.//a[@class="btn72"]')
                                # order_btn.click()
                        elif seat_type == 'M':  # 说明是一等座
                            count = infos[8]
                            if count.isdigit() or count == '有':
                                # 有票后点击预定按钮
                                is_flag = True
                                break  # 退出遍历席位的循环

                    if is_flag: # 判断是否有余票，有余票则执行点击预定按钮操作
                        self.selected_no=train_no # 此时将点击预定的车次信息赋值给self.selected_no属性
                        order_btn = train.find_element_by_xpath('.//a[@class="btn72"]')
                        order_btn.click()
                        # break # 点击预定按钮后，退出遍历车次的循环,没有while循环时候要用break
                        return # 退出函数


            # print(info.text)

    def comfirm(self):
        # 等待来到确认乘车人页面
        WebDriverWait(driver,1000).until(
            ec.url_to_be(self.confirm_url)
        )
        # 等待乘车人信息加载出来
        WebDriverWait(driver,1000).until(
            ec.presence_of_all_elements_located((By.XPATH,'//ul[@id="normal_passenger_id"]/li/label'))
        )
        #获取所有乘车人
        passengers=driver.find_elements_by_xpath('//ul[@id="normal_passenger_id"]/li/label')
        for passenger in passengers:# passenger是label标签
            name=passenger.text
            # print(name)
            if name in self.passenger_name_list:
                passenger.click() # label标签点击
        #确认坐席
        seat_select=Select(driver.find_element_by_id('seatType_1'))
        seat_types=self.trains[self.selected_no] # 根据key获取值，self.trains是要抢票的车次的字典,self.selected_no是要抢票的键
        for seat_type in seat_types:
            try:
                seat_select.select_by_value(seat_type)
                self.selected_seat=seat_type #记录有票的坐席
            except NoSuchElementException:  # 判断席位不存在，捕获异常后继续执行循环
                continue
            else:
                break #判断下拉选择框中有想要的坐席，则退出循环，可以点击提交订单了

        WebDriverWait(driver,1000).until(
            ec.element_to_be_clickable((By.ID,'submitOrder_id')) # 等待a标签（提交订单按钮）可以点击的时候
        )
        # 提交订单
        submit_button=driver.find_element_by_id('submitOrder_id')
        submit_button.click()

        # 显示等待，等到模式对话框窗口出现为止
        WebDriverWait(driver,1000).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME,'dhtmlx_window_active'))
        )
        # 等待窗口上的按钮可以点击
        WebDriverWait(driver,1000).until(
            ec.element_to_be_clickable((By.ID,'qr_submit_id'))
        )
        submit_btn=driver.find_element_by_id('qr_submit_id')
        while submit_btn: # 因为窗口上的按钮很难点上，所以加一个循环，点中后窗口就关闭了，再次获取按钮就获取不到了
            try:
                submit_btn.click()
                submit_btn=driver.find_element_by_id('qr_submit_id')
            except ElementNotVisibleException:
                break
        print(f'恭喜{self.selected_no}车次的{self.selected_seat}坐席抢到了！！！')


    # 负责调用其他方法(组织其他的代码)
    def run(self):
        # 1.登录
        self.login()
        # 2.余票查询
        self.search_ticket()
        # 3.确认乘车人
        self.comfirm()


    # 初始化车站编号（从Excel表中读取）
    def init_station_code(self):
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
    spider = TrainSpider('上海', '连云港', '2020-12-15', {'G8262': ['O', 'M']},['孙陆'])  # o表示的是二等座，M表示一等座
    spider.run()
    spider.init_station_code()


if __name__ == '__main__':
    start()
