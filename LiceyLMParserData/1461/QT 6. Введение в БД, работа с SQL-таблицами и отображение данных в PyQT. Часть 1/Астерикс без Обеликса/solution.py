import sqlite3
con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""
    SELECT title FROM films
    WHERE title LIKE '%Астерикс%' 
    AND title NOT LIKE '%Обеликс%'
""").fetchall()
for elem in map(lambda x: x[0], result):
    print(elem)
con.close()