#author : comma
#date : 2021/2/23 10:25

'''
如果是合数那么必然存在一个 <=√n 的质因数（想想为什么）。于是我们只要枚举 2 到 √n 内的所有数，看看是不是都不能整除
'''
import math
flag=1
count=0

for i in range(1,100):
    x=int(math.sqrt(i))
    for j in range(2,x+1):
        if i%j==0:
            flag=0
            break
    if flag==1:
        count+=1
        print(i)
    flag=1
print(count)