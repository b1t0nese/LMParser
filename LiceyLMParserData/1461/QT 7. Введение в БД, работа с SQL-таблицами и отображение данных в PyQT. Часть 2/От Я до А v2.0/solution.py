def get_result(name):
    import sqlite3
    con = sqlite3.connect(name)
    con.cursor().execute("""DELETE FROM films
        WHERE title like 'Я%а'""")
    con.commit()
    con.close()