#author : comma
#date : 2021/2/23 11:36


s=input('请输入:')
number=0
lower=0
space=0
big=0
for c in s:
    if c.isdigit():
        number+=1
    elif c.islower():
        lower+=1
    elif c.isspace():
        space+=1
    elif c.isupper():
        big+=1
print(number,lower,big,space)