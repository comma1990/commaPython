#author : comma
#date : 2021/2/25 10:56

'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
　　　第10次落地时，共经过多少米？第10次反弹多高？
'''

h=100
s=0
n=eval(input('请输入次数：'))
def fun(n):
    if n==1:
        s=100
        return s
    else:
        s=fun(n-1)+100/(2**(n-1))
        return s

if __name__ == '__main__':
    print(fun(n))


######方法二###########
# s=100
# h=100
# for i in range(2,11):
#     s=s+h/(2**(i-1))
#
# print(s)