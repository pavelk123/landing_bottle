import sqlite3

conn = sqlite3.connect('data.db')
conn.execute('CREATE TABLE data (id INTEGER PRIMARY KEY, name char(100) NOT NULL, email char(100) NOT NULL, subject char(100) NOT NULL, message text NOT NULL)')
conn.execute('INSERT INTO data (name,email,subject,message) VALUES ("Pavel","ads@sdffa","asdad","asdasd")')
conn.execute('CREATE TABLE subs (id INTEGER PRIMARY KEY, email char(100) NOT NULL)')
conn.execute('INSERT INTO subs (email) VALUES ("ads@sdffa")')
conn.commit()
conn.close()

