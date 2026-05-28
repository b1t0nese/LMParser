import sqlite3
con = sqlite3.connect(input())
cur = con.cursor()
genres = cur.execute("""SELECT genre FROM films
    WHERE year = 2010 OR year = 2011""").fetchall()
genres = map(lambda x: cur.execute(f"""SELECT title FROM genres
    WHERE id = {x[0]}""").fetchone()[0], set(genres))
for elem in genres:
    print(elem)
con.close()