import sqlite3
con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT title FROM films WHERE title LIKE '%?'""").fetchall()
for elem in result:
    print(elem[0])
con.close()