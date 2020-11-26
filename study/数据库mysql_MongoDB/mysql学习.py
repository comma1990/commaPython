# author : comma
# date : 2020/11/25 12:27

import mysql.connector


# 创建连接
def insert():
    connector = mysql.connector.connect(host='localhost', user='root', passwd='root', database='comma',
                                        auth_plugin='mysql_native_password')
    # print(connector)
    mycursor = connector.cursor()
    # 编写SQL语句
    sql = 'insert into student (name,Python,sex) values (%s,%s,%s)'
    ############# 单条数据插入 ######################
    # value = ('二豆', 89, 1)     # 单行数据插入
    # 执行SQL语句
    # mycursor.execute(sql, value)  # 单行数据执行

    ############ 批量数据插入 ##################
    values = [('憨憨', 85, '女'), ('渣渣', 58, '女'), ('喵喵', 79, '男')]
    mycursor.executemany(sql, values)

    # 提交
    connector.commit()
    print('插入了', mycursor.rowcount, '条数据')


def update():
    connector = mysql.connector.connect(host='127.0.0.1', port=3306, user='root', passwd='root', database='comma',
                                        auth_plugin='mysql_native_password')
    mycursor = connector.cursor()
    sql = 'update student set name="黄月" where name="黄月英"'
    mycursor.execute(sql)
    connector.commit()
    print('更新了', mycursor.rowcount, '条数据')


def delete():
    connector = mysql.connector.connect(host='127.0.0.1', port=3306, user='root', passwd='root', database='comma',
                                        auth_plugin='mysql_native_password')
    mycursor = connector.cursor()
    sql = 'delete from student where name="喵喵"'
    mycursor.execute(sql)
    connector.commit()
    print('删除了', mycursor.rowcount, '条数据')


if __name__ == '__main__':
    # insert()
    update()
    # delete()
