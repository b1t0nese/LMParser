def get_result(name):
    import sqlite3
    con = sqlite3.connect(name)
    con.cursor().execute("""UPDATE films SET duration = duration*2
        WHERE genre = (SELECT id FROM genres WHERE title = 'фантастика')""")
    con.commit()
    con.close()