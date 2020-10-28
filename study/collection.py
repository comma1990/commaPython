# Author ： comma
# 日期 : 2020/10/15  06:37


####### 字符串的操作 #######
s = 'hello,Python'
print(s.center(20, '*'))    # 居中对齐，第一个参数指定宽度，第二个参数指定填充符，如果宽度小于字符串本身，返回字符串本身
print(s.ljust(20, '*'))     # 左对齐，第一个参数指定宽度，第二个参数指定填充符，如果宽度小于字符串本身，返回字符串本身
print(s.rjust(20, '*'))     # 右对齐，第一个参数指定宽度，第二个参数指定填充符，如果宽度小于字符串本身，返回字符串本身
print(s.zfill(20))      # 右对齐，只有一个参数指定宽度，左边用0填充，如果宽度小于字符串本身，返回字符串本身，如果字符串带'-'，0在'-'右边添加
print(s.zfill(5))
print('-8910'.zfill(10))

######### 字典常用方法 ###########
# score = {'逗号': 30, '二豆': 24}
# print('逗号' in score)  # 判断键是否在字典中
# score['憨憨'] = 26  # 添加元素
# print(score)
# del score['憨憨']  # 删除元素
# print(score)
# print(score.keys())  # 获取所有的键
# print(score.values())  # 获取所有的值
# print(list(score.values()))  # 将获取的值转换成列表，键也同样操作
# print(score.items())  # 获取所有的元素
# print(list(score.items()))  # 将获取的键值对转换成元组
# for item in score:
#     print(item, score[item], score.get(item))  # 字典的遍历，循环获取的是减值，score[key]获取值的时候，如果key不在字典中会报错，get方法则会返回None
# # 字典生成式,定义两个数组，使用zip方法进行打包,生成字典的时候按照短的列表来匹配，长列表多余截取
# nikename = ['花花', 'Hebe', '雨神']
# name = ['华晨宇', '田馥甄', '萧敬腾', '林宥嘉']
# match = {x: y for x, y in zip(nikename, name)}
# print(match)

############### 元组的使用 ##### = tuple(('python', '皮皮', 3333))  # tuple方法中要嵌套一层小括号
# t2 = (10,)  # 只包含一个元素的时候要使用逗号和小括号
# print(t, t1, t2, t3)

###### eval方法的使用 ###########
# x = input('请输入一个数字：')
# print(type(x), type(eval(x)))   # eval()去掉字符串最外侧的引号，如input函数得到的数据类型是str，去掉外侧的引号，就变成输入数据本身的类型了
# num = eval(x) + 1               # 注意：input函数输入的是字符串类型再用eval函数会报错
# print(num)


# 记录学习过程中常用的方法
############ random获取随机数 ##############
# import random
#
# print(random.random())  # 产生一个[0，1）之间的随机数
# print(random.randint(1, 20))  # 产生一个1-20之间的随机数
# print('-------')
# for i in range(1, 10):
#     print(random.randrange(2, 20, 2), end='\t')  # 产生一个[2,20)之间的随机数，步长为2，所以都是偶数
# print('------')
# lst = [1, 20, 23, 44, 87, 22, 11, 8, 30]
# print(random.choice(lst))  # 随机获取一个列表中的元素
# random.shuffle(lst)  # 打乱列表顺序
# print(lst)
################################################

# time模块
# import time
# print(time.time()) #打印当前时间的时间戳
#
# print(time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime()))  #格式化当前时间为：2020-10-15T07:13:59
#
# import datetime
# #获取当前时间
# now=datetime.datetime.now();
# #时间偏移量
# add=datetime.timedelta(minutes=10)
# #当前时间+时间偏移量
# data=now+add
# print(data.strftime('%Y-%m-%d %H:%M:%S')) #格式化时间
