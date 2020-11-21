# @Author  :  comma 
# @Date    :  2020-11-21 15:45

'''
CSV文件的操作：
向csv文件中写入数据：
    引入csv模块
    使用open()函数创建csv文件
    借助csv.writer()函数创建writer对象
    调用writer对象的writerow()方法写入一行数据
    调用writer对象的writerows()方法写入多行数据

从csv文件中读取数据：
    引入csv模块
    使用open()函数打开csv文件
    借助csv.reader()函数创建reader对象
    读到的每一行都是一个列表


'''
import csv

######### 向csv文件写入数据 ################
# with open('csv存储数据.csv', 'a+', newline='') as file:
#     writer = csv.write(file)
#     # 一次写一行数据
#     writer.writerow(['逗号', 30, 88])
#     # 一次写多行
#     lst = [['二豆', 24, 90], ['渣渣', 28, 80]]
#     writer.writerows(lst)

########## 从csv读取数据 ##################
with open('csv存储数据.csv','r',newline='') as file1:
    reader=csv.reader(file1)
    for item in reader:
        print(item)