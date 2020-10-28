# Author ： comma
# 日期 : 2020/10/28  21:26


######## 查找 #########
ss = 'hello,python,python'
print(ss.index('python', 0, 20))  # 查找指定字符第一次出现的位置，第一个参数指定'子字符串'，第二个参数指定开始位置，第三参数指定结束位置，二三参数可省略
print(ss.rindex('python'))  # 查找字符串最后一次出现的位置，即：从右查找，返回的索引是从左开始数的
print(ss.find('python'), ss.find('java'))  # 查找字符串第一次出现时的索引，当字符串不存在时，返回-1
print(ss.rfind('python'))  # 查找字符串最后一次出现时的索引，当字符串不存在时，返回-1

############# 字符串的比较 #################
# 两个字符进行比较的时候，比较的是ordinal value（原始值），调用指定函数ord可以得到字符的原始值，对应的chr函数可以得到原始值对应的字符
print(ord('a'))  # a对应的原始值是97，即：ASCII 码
print(chr(97))

######### 大小写转换 ############
print('comma'.upper())  # 把所有字符串转换成大写
print('Comma'.lower())  # 把所有字符串转换成小写
print('Comma'.swapcase())  # 把所有大写字母转换成小写字母，把所有小写字母转换成大写字母
print('hello，Java'.capitalize())  # 把第一个字符转换成大写，其它转换成小写
print('hello pyThon'.title())  # 把每个单词的第一个字符转换成大写，剩余字符转换成小写

######## 对齐 #####
s = 'hello,Python'
print(s.center(20, '*'))  # 居中对齐，第一个参数是指定宽度（小于字符宽度时，输出字符串本身），第二个参数是指定填充字符，不填默认是空
print(s.ljust(20, '*'))  # 左对齐,第一个参数是指定宽度，第二个参数是指定填充字符，不填默认是空
print(s.rjust(20))  # 右对齐，第一个参数是指定宽度，第二个参数是指定填充字符，不填默认是空
print(s.zfill(20))  # 右对齐，只有一个参数，指定字符串宽度，左边用0填充
print('-87654'.zfill(20))  # -0000000000000087654,当有'-'时，0在'-'右边填充

######## 字符串拆分 #########
s1 = 'python,hello,python,python,java'
print(s1.split(sep=','))  # 通过sep指定分割符拆分字符串，默认是空字符串，拆分结果是一个列表,sep可以省略不写
print(s1.split(sep=',', maxsplit=2))  # maxsplit指定最大拆分次数，maxsplit关键字可以省略
print(s1.split(',', 3))
# 下面是从右往左拆分
print(s1.rsplit(',', 3))  # 拆分三次后，剩余的字符串放一块，所以列表中有4个元素

######### 字符串的判断 ############
print('_hello_124555'.isidentifier())  # 判断字符串是不是合法的标识符，合法标识符有：字母，数字，下划线（必须以字母或者下划线开头）。其它都是非法的。
print('\r\n\t'.isspace())  # 判断字符串是否全部是空白字符组成（回车\r，，换行\n，水平制表符\t）
print('abcde'.isalpha(), '逗号'.isalpha())  # 判断字符串是不是全部由字母组成,中文也是字母
print('0123456789'.isdecimal())  # 判断字符是不是全部由十进制的数字组成
print('0987654321三'.isnumeric())  # 判断字符串是不是全部由数字组成，中文一二三四也是数字
print('abc1234'.isalnum())  # 判断字符串是不是全部由字母和数字组成

####### 字符串的替换与拼接操作 ############
s2 = 'python,hello,java,python,comma'
print(s2.replace('python', 'java', 1))  # 第一个参数指定要替换的字符，第二个参数指定替代字符，第三个参数指定替换次数
lst = ['hello,', 'python,', 'I\'m comma']
tup = ('小猫', '喜欢', '小狗', '987')
print(''.join(lst))  # 将列表活元组中的字符串合并成一个字符串,列表或者元组中元素必须都是字符串，数字要用引号引起来
print('_'.join(tup))  # 小猫My喜欢My小狗;通过'_'来连接元素
print('-'.join('python'))  # 会把字符串转换成列表然后连接

######### 字符串截取操作（切片） ##############
sq = 'hello,python'
print(sq[:5])  # 从索引为0的位置开始，截取到索引为5（不包括5）的位置
print(sq[6:])  # 从索引为6的位置开始，截取到最后
print(sq[1:5:2])  # 从索引为1的位置开始，到索引为5的位置结束，步长为1
print(sq[::1])  # 不指定开始位置和结束位置，只设置步长，正序输出字符串
print(sq[::-1])  # 不指定开始和结束位置，只设置步长-1，倒着输出字符串

######### 格式化字符串 （定义变量在字符串中使用）###############
dic = {'小明': 31, '小郭': 30}
# %做占位符，%s字符串，%d活%i整数，%f浮点数
for name in dic:
    print(name, dic.get(name))
    print('%s今年%d岁了' % (name, dic.get(name)))
    print('{0}今年{1}岁了'.format(name, dic.get(name)))  # {}中的数字是format中元素位置的索引format相当于一个元组，从元组中取数据
    print(f'{name}今年{dic.get(name)}岁了')

print('{0}今年{2}岁了'.format('小红', '5', '8'))
print('%10d' % 3457)  # 10标识宽度，宽度不够时，左边以空格占位
print('%.3f' % 3.141592657)  # .3表示只保留三位小数
print('%10.3f' % 3.141592657)  # 10表示宽度，.3表示保留三位小数
print('{0:.3}'.format(3.141592657))  # 0表示占位符(可以省略不写)，取索引为0的元素，.3表示保留三位数
print('{0:10.3f}'.format(3.141592657))  # 0表示占位符(可以省略不写)，取索引为0的元素，10表示宽度，.3表示保留三位小数

######## 编码与解码 ############
sb = '好好学习，天天向上'
print(sb.encode(encoding='GBK'))  # GBK编码中，一个中午占两个字节
print(sb.encode(encoding='UTF-8'))  # UTF-8中，一个字符占三个字节
byte = sb.encode('GBK')
print(byte.decode('GBK'))
byte1=sb.encode('UTF-8')
print(byte1.decode('utf-8'))    # 不区分大小写