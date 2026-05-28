import sqlite3
con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT title FROM films
    WHERE duration <= 85
""").fetchall()
for elem in map(lambda x: x[0], result):
    print(elem)
con.close()