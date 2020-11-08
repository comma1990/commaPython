# @Author  :  comma 
# @Date    :  2020-11-07 18:22


'''
文件的打开模式
w ：写入权限，会覆盖文件原有内容，没有文件会新建一个文件
a ：文件写入权限，在文件原有内容后追加，没有文件会新建
r ：只读模式打开文件，文件的指针会放在文件的开头
b ：以二进制方式打开文件，不能单独使用，需要和其它模式一起使用，入：rb，wb
+ ：以读写方式打开文件，不能单独使用，需要和其它模式一起使用，如：a+
'''

file = open('/Users/sun/Desktop/文件写入测试.txt', 'w')  # w写入权限，会覆盖文件原有内容，没有文件会新建一个文件
file.write('文件写入测试')
file.close()

file1 = open('/Users/sun/Desktop/文件写入测试.txt', 'a')  # a文件写入权限，在文件原有内容后追加，没有文件会新建

# 拷贝文件 rb,wb组合使用，通常用来拷贝图片，音频，视频
src_file = open('/Users/sun/Downloads/原图.png', 'rb')
target_file = open('/Users/sun/Downloads/复制.png', 'wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()

'''
文件对象的常用方法
read([size]):从文件中读取size个字节或字符的内容返回，若省略size，则读取到文件末尾，即读取文件所有内容
readline():从文本文件中读取一行内容
readlines():把文本文件中每一行都作为一个独立的字符串对象，并将这些对象放入列表返回
write(str):将字符串str内容写入文件
writelines(s_list):将字符串列表s_list写入文本文件，不添加换行符
seek(offset[,whence]):
tell(): 返回文件指针的当前位置
flush(): 把缓冲区的内容写入文件，但不关闭文件
close(): 把缓冲区的内容写入文件，同时关闭文件，释放文件对象的相关资源
'''
s = ['\n你好', 'comma', '今天学Python了吗？']
file2 = open('/Users/sun/Desktop/文件写入测试.txt', 'a')
file2.writelines(s)
file2.close()

file3 = open('/Users/sun/Desktop/文件写入测试.txt', 'r')
print(file3.read(2))
print(file3.readlines())
file3.close()
