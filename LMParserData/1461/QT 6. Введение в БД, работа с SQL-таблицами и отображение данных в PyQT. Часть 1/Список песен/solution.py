import sqlite3
con = sqlite3.connect("music_db.sqlite")
cur = con.cursor()
result = cur.execute("""
    SELECT DISTINCT Name FROM Track
    WHERE AlbumId IN (
        SELECT AlbumId FROM Album 
        WHERE ArtistId = (
            SELECT ArtistId FROM Artist 
            WHERE Name = ?))
    ORDER BY Name
""", (input(),)).fetchall()
for elem in map(lambda x: x[0], result):
    print(elem)
con.close()