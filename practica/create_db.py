import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("CREATE TABLE if not exists user (name text, mail text, password text)")

conn.commit()
conn.close()
