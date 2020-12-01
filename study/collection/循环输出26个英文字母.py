#author : comma
#date : 2020/12/1 18:04

'''
循环打印26个英文字母
# 两个字符进行比较的时候，比较的是ordinal value（原始值），调用指定函数ord可以得到字符的原始值，对应的chr函数可以得到原始值对应的字符
print(ord('a'))  # a对应的原始值是97，即：ASCII 码
print(chr(97))
'''
for i in range(26):
    item=chr(ord('a')+i)
    print(item,end='\t')