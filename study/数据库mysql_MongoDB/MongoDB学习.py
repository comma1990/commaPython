# @Author  :  comma 
# @Date    :  2020-11-27 22:43


import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
# 获取要操作的数据库，下面两种方式
# db=client.comma
db = client['comma']

# 获取要操作的集合（表）
# collection=db.student
collection=db['student']

print(collection)
# 插入数据
# stu1={'name':'天明','age':30,'sex':'男'}
# collection.insert_one(stu1)
# 插入多条数据
stu_list=[{'name':'高月','age':16},{'name':'少羽','sex':'男'},{'name':'盖聂','age':35}]
collection.insert_many(stu_list)

