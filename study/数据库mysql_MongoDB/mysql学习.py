# author : comma
# date : 2020/11/25 12:27

import mysql.connector

# 创建连接
connector = mysql.connector.connect(host='172.17.22.86',port=3306, user='root', passwd='root', database='comma',
                                    auth_plugin='mysql_native_password')
# print(connector)
mycursor = connector.cursor()

# 编写SQL语句
sql = 'insert into student (name,Python,sex) values (%s,%s,%s)'
value = ('二豆', 89, 1)

# 执行SQL语句
mycursor.execute(sql, value)

# 提交
connector.commit()

print('插入了', mycursor.rowcount, '条数据')
