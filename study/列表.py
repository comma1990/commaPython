# @Author  :  comma 
# @Date    :  2020-10-31 20:38


#### 列表、字典、元组、集合总结 ######
# 数据结构      是否可变        是否重复        是否有序        定义符号
# 列表（list）    可变           可重复          有序           []
# 元组（tuple）  不可变          可重复           有序          ()
# 字典（dict）    可变         key不可重复，
#                            value可以重复      无序          {key:value}
# 集合（set）     可变           不可重复         无序           {}


########列表的操作：#################

def operation():
    list1 = [0, 9, 5, 7, 2, 3]
    list1.remove(2)  # 移除指定的元素
    list1.pop(1)  # 根据索引移除元素，如果不指定索引位置，将列表的最后一个元素移除
    list1.clear()  # 清空列表
    list2 = list1[1:3]  # 切片，取指定索引范围内的元素，删除指定索引范围内的数据：list1[1:3]=[]
    del list1  # 删除列表对象
    print(list1)

# 排序
def sort():
    list1 = [0, 9, 5, 7, 2, 3]
    # list1.sort()  # 升序
    # list1.sort(reverse=True)  # 倒序
    print(list1)
    # print(sorted(list1))  # 内置函数
    print(sorted(list1, reverse=True))  # 先升序排序，然后翻转，就是倒序

# 列表表达式
def expression():
    list2 = [i * i for i in range(1, 10, 2)]  # 范围1-10，步长为2，遍历结果是1，3，5，7，9；遍历结果自相乘
    print(list2)

####################################


# #空列表的bool值为False
def bool():
    x = []
    print(bool(x))

if __name__ == '__main__':
    sort()