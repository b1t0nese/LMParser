def get_result(name):
    import sqlite3
    con = sqlite3.connect(name)
    con.cursor().execute("""UPDATE films SET duration = duration/3
        WHERE year = 1973""")
    con.commit()
    con.close()