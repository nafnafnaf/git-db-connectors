import sqlite3

import subprocess

db = r'C:\Users\nafnaf\SQLITE\db\pythonsqlite.db'
conn = sqlite3.connect(db)
if conn:
    print('connected')

insert_query = """INSERT INTO Laptop
               (Id, Name, Price, Date)
               VALUES (?,?,?,?)"""

records_list = [(4, 'HP Pavilion Power', 1999, '2019-01-11'),
                     (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
                     (6, 'Microsoft Surface', 2330, '2019-07-23')]

cur = conn.cursor()
cur.executemany(insert_query, records_list)
conn.commit()
print("Number of records after inserting rows:")
cursor = cur.execute('select * from Laptop;')
print(len(cursor.fetchall()))
if conn:
    print("\nThe SQLite connection is closed.")
# subprocess = subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE)
# subprocess_return = subprocess.stdout.read()
# print(subprocess_return)


# =============== PLACEHOLDERS SQL INJECTION ========================
#
# cur = con.cursor()
# list = [1,2,3]
#
# # Create a placeholder list containing a '?' for each element
# placeholders = []
# for i in list:
#     placeholders.append('?')
# # Change placeholder list to string of question marks separated by commas
# ph_text = ', '.split(placeholders)
#
# # Create sql statement
# # Can use format here without risk of SQL injection because it is only ', ' and '?'
# sql = """SELECT * FROM data d WHERE d.field IN ({0})""".format(ph_text)
#
# # Execute the statement, passing list items in tuple for fdb to escape (avoid SQL-injection)
# # Note that the list is converted to a tuple,
# # whereas the SQL in the question had the list as the first (and only) tuple element
# cur.execute(sql, tuple(list))
