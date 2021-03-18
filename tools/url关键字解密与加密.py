#author : comma
#date : 2021/3/18 16:13
import urllib.parse

'''解密'''
def parse(word):
    w=urllib.parse.unquote(word)
    print(w)

'''加密'''
def encode(key):    #key需要是字典类型
    k=urllib.parse.urlencode(key)
    print(k)

if __name__ == '__main__':
    flag=eval(input('1、解析字符串，2、加密字符串\n请选择：'))
    if flag==1:
        w=input('请输入要解密的字符串：')
        parse(w)
    elif flag==2:
        k=input('请输入要加密的字符串：')
        keyword={'key':k}
        encode(keyword)
    else:
        print('输入有误')