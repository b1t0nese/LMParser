import sqlite3
con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT year FROM films WHERE title LIKE 'Х%'""").fetchall()
for elem in map(lambda x: x[0], set(result)):
    print(elem)
con.close()