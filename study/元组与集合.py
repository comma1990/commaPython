# @Author  :  comma 
# @Date    :  2020-10-31 22:21


########### 集合 #############
def operation():
    ses = set('python')  # set()方法中可以放列表，元组，字符串；——定义空集合只能用set() s=set()
    print(ses)
    s = {10, '小猫', 40}
    s.add('皮皮')  # 添加元素，单个元素
    print(s)
    s.update([20, 30])  # 一次添加多个元素,以列表方式
    s.update((50, 60))  # 一次添加多个元素,以元组方式
    s.update({101, 102, 103})  # 以集合方式添加
    print(s)
    # s.remove(80)    # 一次移除一个元素 ，元素不存在时会报错
    s.discard(90)  # 移除指定的元素，如果元素不存在不会报错
    # s.pop()  # 随机删除一个元素,不能指定参数
    # print(s)
    print('皮皮' in s)  # 判断元素是否在集合中，判断元素不在集合中 not in
    #
    # s.clear()  # 清空集合


def op():
    s1 = {10, 20, 30, 40, 5}
    s2 = {10, 20, 30, 40, 50, 60}

    print(s1.issubset(s2))  # 判断s1是不是s2的子集
    print(s2.issuperset(s1))  # 判断s2是不是s1的超集（即：s2包含s1）
    print(s1.isdisjoint(s2))  # 两个集合没有交集时isdisjoin()返回True，有交集时返回False

    print(s1.intersection(s2))  # 求两个集合的交集 与&等价
    print(s1 & s2)

    print(s1.union(s2))  # 求两个集合的并集,与 | 等价
    print(s1 | s2)

    print(s1.difference(s2))  # 求两个集合的差集，与 - 等价，只输出s1中与s2不同的元素，不包括s2中独有的元素
    print(s2.difference(s1))
    print(s2 - s1)

    print(s1.symmetric_difference(s2))  # 对称差集,两个集合的不同元素全部输出，与 ^ 等价
    print(s1 ^ s2)

# 集合生成式
def op2():
    print({i * i for i in range(10)})

############### 元组的使用 #####
def tup():
    tup = tuple(('python', '皮皮', 3333))  # tuple方法中要嵌套一层小括号
    t2 = (10,)  # 只包含一个元素的时候要使用逗号和小括号

    for item in tup:  # 元组的遍历
        print(item)

if __name__ == '__main__':
    # operation()
    op2()