# @Author  :  comma 
# @Date    :  2020-11-27 22:43


import pymongo


def insert():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    # 获取要操作的数据库，下面两种方式
    # db=client.comma
    db = client['comma']

    # 获取要操作的集合（表）
    # collection=db.student
    collection = db['student']

    print(collection)
    # 插入数据
    # stu1={'name':'天明','age':30,'sex':'男'}
    # collection.insert_one(stu1)
    # 插入多条数据
    stu_list = [{'name': '高月', 'age': 16}, {'name': '少羽', 'sex': '男'}, {'name': '盖聂', 'age': 35}]
    collection.insert_many(stu_list)


def update():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client['comma']
    collection = db['student']
    # 修改一条数据
    collection.update_one({'name': '高月'}, {'$set': {'sex': '女'}})
    # 修改多条数据
    collection.update_many({'name': '卫庄'}, {'$set': {'sex': '男'}})


def remove():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client['comma']
    collection = db['student']
    # 一次删除一条数据
    collection.delete_one({'name': '卫庄', 'age': 24})
    # 一次删除多条数据
    collection.delete_many({'name': '鲁班'})


def find():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client['comma']
    collection = db['student']
    # 查询
    result = collection.find()
    for item in result:
        print(item)
    print('----------1-------------------')

    luban = collection.find({'name': '鲁班'})
    for item in luban:
        print(item)
    print('-----------2------------------')
    # 模糊查询
    regex = collection.find({'name': {'$regex': '.*庄.*'}})
    for item in regex:
        print(item)
    print('------------3-----------------')
    # 排序 pymongo.ASCENDING升序,pymongo.DESCENDING降序
    asc = collection.find().sort('age', pymongo.DESCENDING)
    for item in asc:
        print(item)
    print('-------------4----------------')

    # 降序后跳过前三条数据，查第四和第五条数据
    asc = collection.find().sort('age', pymongo.DESCENDING).skip(3).limit(2)
    for item in asc:
        print(item)
    print('------------5-----------------')


if __name__ == '__main__':
    # insert()
    # update()
    # remove()
    find()
