import sqlite3


db = r'C:\Users\nafnaf\SQLITE\db\pythonsqlite.db'
conn = sqlite3.connect(db)
if conn:
    print('connected')
select = """SELECT * FROM Laptop"""
cur = conn.cursor()
cur.execute(select)
rows = cur.fetchall()

for row in rows:
    print(row)