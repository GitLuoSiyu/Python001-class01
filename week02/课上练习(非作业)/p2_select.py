import pymysql

conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'root',
    database = 'geek',
    charset = 'utf8mb4'
)

# 获取cursor游标对象
con1 = conn.cursor()

# 操作的行数
count = conn1.execute('select * from geek')
print(f'查询到 {count} 条记录')

# 获取一条查询结果
result = con1.fetchone()
print(result)

# 获取所有的查询结果
print(conn1.fetchall())

con1.close()
conn.close()

# 批量插入操纵
# values = [{id, 'testuser} + str(id) for id in range(4, 21)]
# cursor.executemany('INSERT INFO' + TABLE_NAME + 'values(%s, %s)', values)










