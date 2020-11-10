# @Author  :  comma 
# @Date    :  2020-10-31 20:42


######### 字典常用方法 ###########
score = {'逗号': 30, '二豆': 24}
print('逗号' in score)  # 判断键是否在字典中
score['憨憨'] = 26  # 添加元素
print(score)
del score['憨憨']  # 删除元素
print(score)
print(score.keys())  # 获取所有的键
print(score.values())  # 获取所有的值
print(list(score.values()))  # 将获取的值转换成列表，键也同样操作
print(score.items())  # 获取所有的元素
print('--------------')
print(list(score.items()))  # 将获取的键值对转换成元组
for item in score:
    print(item, score[item], score.get(item))  # 字典的遍历，循环获取的是减值，score[key]获取值的时候，如果key不在字典中会报错，get方法则会返回None
# 字典生成式,定义两个数组，使用zip方法进行打包,生成字典的时候按照短的列表来匹配，长列表多余截取
nikename = ['花花', 'Hebe', '雨神']
name = ['华晨宇', '田馥甄', '萧敬腾', '林宥嘉']
match = {x: y for x, y in zip(nikename, name)}
print(match)




