# @Author  :  comma 
# @Date    :  2021-02-18 10:23


ptext=input('请输入明文文本：')
for p in ptext:
    if 'a'<p<'z':
        print(chr(ord('a')+(ord(p)-ord('a')+3)%26))
        # print(chr(ord(p)+3),end='')

# print(chr(ord('a')+3))