import dbf

table = dbf.Table(filename='VORIA.DBF',on_disk=True)

print(table)
print(type(table))