import sqlite3
con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT title FROM films
    WHERE year > 1996 AND (genre = (
        SELECT id FROM genres
        WHERE title = 'анимация') OR genre = (
        SELECT id FROM genres
        WHERE title = 'музыка'))""").fetchall()
for elem in result:
    print(elem[0])
con.close()