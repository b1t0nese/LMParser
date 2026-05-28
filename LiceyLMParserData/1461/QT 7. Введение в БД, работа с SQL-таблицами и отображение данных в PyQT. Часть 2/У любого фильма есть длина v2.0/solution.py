def get_result(name):
    import sqlite3
    con = sqlite3.connect(name)
    con.cursor().execute("""UPDATE films SET duration = 42
        WHERE duration IS NULL OR duration = '' OR duration = 0""")
    con.commit()
    con.close()