#author : comma
#date : 2020/11/25 16:03

import mysql.connector

host='172.16.101.211'
port=30001
name='productsearch_user'
passwd='q#@!123a'
connector=mysql.connector.connect(host=host,port=port,user=name,passwd=passwd,database='productsearch',auth_plugin='mysql_native_password')
# print(connector)  #测试连接
mycursor=connector.cursor()
sql='select * from suggest_items where sellerId=500041475'
mycursor.execute(sql)
result=mycursor.fetchall()
print(type(result))
for item in result:
    print(item)