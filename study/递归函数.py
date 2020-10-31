# @Author  :  comma 
# @Date    :  2020-10-31 16:26


# 递归函数  ——函数本身调用本身，递归的组成部分：①调用条件②终止条件 即：if...else...


# ——阶乘（...6*5*4*3*2*1）
def fac(n):
    if n == 1:
        return 1
    else:
        result = n * fac(n - 1)
        return result


print(fac(6))
print('--------------------')


# 斐波那契数列 1，1，2，3，5，8，13，21，34......规律：第三个数开始，是前两个数相加之和
def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)


print(fibo(8))
