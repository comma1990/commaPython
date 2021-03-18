#author : comma
#date : 2021/2/22 15:19

for i in range(1,10):
    for j in range(1,i+1):
        result=i*j
        print(f'{j}*{i}={result}',end='\t')
    print('')