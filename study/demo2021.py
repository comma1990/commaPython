#author : comma
#date : 2021/1/7 17:34

import  random
list1=[chr(i) for i in range(97,123)]
list2=[i for i in range(0,10)]
lst=list1+list2
# print(lst)
for i in range(0,10):
    for j in range(0,8):
        print(random.choice(lst),end='')
    print()




#
# lst=[(1,4),(2,3),(4,1)]
# lst.sort(key=lambda x:x[0],reverse=False)
# print(lst)


#
# txt=input('请输入：')
# d={}
# for i in txt:
#     d[i]=d.get(i,0)+1
# print(d)
#
# # print(d.items())
# ls=list(d.items())
# ls.sort(key=lambda x:x[1],reverse=True)



# s='abcbad'
# if s==s[::-1]:
#     print('yes')
# else:
#     print('false')

# print(s[::-1])