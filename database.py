import sqlite3
con=sqlite3.connect("form.db")
c=con.cursor()
c.execute('''create table if not exists user(ID text primary key,name text,family text,web text,network text,programming text,age text) ''')
con.commit()
con.close()
