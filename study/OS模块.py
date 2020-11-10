# @Author  :  comma 
# @Date    :  2020-11-08 16:12

'''
os.path操作目录相关函数
abspath（path）：用于获取文件或者目录的绝对路径
exists(path)：用于判断文件或者目录是否存在，如果存在返回True，不存在返回False
join(path,name)：将目录与目录或者文件名拼接起来
splitext() ：分离文件名和扩展名
basename(path) ：从一个目录中提取文件名
dirname(path) ：从一个路径中提取文件路径，不包括文件名
isdir(path) ：用于判断是否为路径
'''

import os
import os.path

# 遍历一个路径下面的所有文件，和子目录
lst_files = os.walk(
    '/Users/sun/PycharmProjects/commaPython')  # walk()返回一个迭代器对象,迭代器里每一个元素都是一个元组，每一个元组都由三部分组成：路径，子目录（列表），文件名（列表）
for dirpath,dirname,filename in lst_files:
    for dir in dirname:
        print(os.path.join(dirpath,dir))
    for file in filename:
        print(os.path.join(dirpath,file))
    print('-----------------------')


# os.system('notepad.exe')    # 打开记事本
# os.system('calc.exe')   # 打开计算器
# os.startfile('C:\\program file\\qq\\qq.exe')
# print(os.getcwd())  # 返回当前的工作目录
#
# lst=os.listdir('../study')  # 返回指定路径下的文件和目录信息 '/Users/sun/PycharmProjects/commaPython'
# print(lst)
#
# os.mkdir('测试目录-可删') # mkdir创建目录
# os.makedirs('测试目录2-可删/子目录') # makedirs创建多级目录
#
# os.rmdir('测试目录-可删')
# os.removedirs('测试目录2-可删/子目录')

########### os.path函数使用 ##############
# print(os.path.split('/Users/sun/PycharmProjects/商品信息.xlsx'))  # 分离路径和文件名
# print(os.path.splitext('商品信息.xlsx'))  # 分离文件名和文件格式后缀
#
# print(os.path.basename('/Users/sun/PycharmProjects/商品信息.xlsx')) # 提取路径中的文件名
# print(os.path.dirname('/Users/sun/PycharmProjects/商品信息.xlsx'))  # 提取路径，不包含文件名


#### 案例：列出指定目录下的所有png格式的文件 ###########

lst = os.listdir('/Users/sun/Downloads')
for item in lst:
    if item.endswith('.png'):
        print(item)
