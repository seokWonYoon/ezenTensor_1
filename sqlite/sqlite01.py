import sqlite3
con = sqlite3.connect('sqlite3.db')
query = '''CREATE TABLE IF NOT EXISTS sales(
        mbr VARCHAR(10),
        product VARCHAR(10),
        amount NUMBER,
        date DATE default current_timestamp
    );
    '''

con.execute(query)
con.commit()

data = [
    ('lee', 'phone', 50),
    ('kim', 'tv', 150),
    ('park', 'phone2', 30),
    ('song', 'tea', 20)
]

stmt = 'INSERT INTO sales(mbr,product,amount)  VALUES(?,?,?)'
con.executemany(stmt,data)
con.commit()

cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()
row_counter = 0
for i in rows:
    print(i)
    row_counter += 1
print("회원수 {}".format(row_counter))