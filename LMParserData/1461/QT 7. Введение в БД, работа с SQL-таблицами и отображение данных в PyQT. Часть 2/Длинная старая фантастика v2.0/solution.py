def get_result(name):
    import sqlite3
    con = sqlite3.connect(name)
    con.cursor().execute("""DELETE FROM films
        WHERE genre = (SELECT id FROM genres
            WHERE title = 'фантастика') AND year < 2000
                AND duration > 90""")
    con.commit()
    con.close()