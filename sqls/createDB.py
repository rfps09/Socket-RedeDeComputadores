import sqlite3

open('prj_redes.db', 'x')

conn = sqlite3.connect('prj_redes.db')
cur = conn.cursor()

f = open('sqls/createTables.sql', 'r', encoding='utf-8')
create_querys = f.read()
f.close()

querys = create_querys.split(';')

for query in querys:
    cur.execute(query)
    conn.commit()

f = open('sqls/insertData.sql', 'r', encoding='utf-8')
insert_querys = f.read()
f.close()

querys = insert_querys.split(';')

for query in querys:
    cur.execute(query)
    conn.commit()

cur.close()
conn.close()