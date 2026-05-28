def get_result(name):
    import sqlite3
    con = sqlite3.connect(name)
    con.cursor().execute("""UPDATE films SET duration = 100
        WHERE genre = (SELECT id FROM genres
            WHERE title = 'мюзикл') AND duration > 100""")
    con.commit()
    con.close()