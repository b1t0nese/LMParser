import sqlite3
con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT title FROM films
    WHERE year >= 1995 AND year <= 2000
    AND genre = (
        SELECT id FROM genres
        WHERE title = 'детектив')
""").fetchall()
for elem in map(lambda x: x[0], result):
    print(elem)
con.close()