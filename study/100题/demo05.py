# @Author  :  comma 
# @Date    :  2021-01-24 13:31
l=[]
a=0
x=eval(input('请输入第一个数：'))
y=eval(input('请输入第二个数：'))
z=eval(input('请输入第三个数：'))
if x<y :
    if y<z:
        l.append(x)
        l.append(y)
        l.append(z)
    else:
        l.append(x)
        l.append(z)
        l.append(y)
elif x<z:
        l.append(y)
        l.append(x)
        l.append(z)
else:
    l.append(z)
    l.append(y)
    l.append(x)


print(l)


# for i in range(3):
