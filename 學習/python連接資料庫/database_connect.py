import pymssql

conn = pymssql.connect(
    host = 'localhost',
    port='1',
    user = '',
    password = '',
    database = '',
)
cursor = conn.cursor(as_dict = True)
#
cursor.execute('select * from dbo.customers')

'''
for row in cursor:
    for row2 in row:
        print(row2)
'''

for row in cursor:
    print(type(row))
    print(row)

'''
tuple 有以下幾個優點：

因為不可變（immutable）的特性，運作起來比串列還要快。
不會不小心改變 tuple 的值，也就是 tuple 的項目不會不小心被更動到。
占用的空間比較少。
作為字典（dictionary）的鍵（key）使用，因為字典的鍵需要不可變的值。
具名 tuple 可以簡易的作為物件的替代品。
'''