import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-VI19T5U\SQLEXPRESS;'
                      'Database=gynext_db_v3_2;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('SELECT brand_name FROM c2g_product_brands WHERE user_text01 is NOT NULL')
#cursor.execute('Select * from schema_name.table_name')
# cursor.execute('SELECT C.TABLE_NAME, C.COLUMN_NAME'
# FROM 'INFORMATION_SCHEMA.COLUMNS C'
# WHERE EXISTS ('SELECT 1 FROM INFORMATION_SCHEMA.TABLES T'
#               WHERE T.TABLE_TYPE='BASE TABLE' AND C.TABLE_NAME=T.TABLE_NAME)
# ORDER BY C.TABLE_NAME, C.COLUMN_N
for row in cursor:
     print(row)