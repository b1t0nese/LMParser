import sqlite3

conn = sqlite3.connect('music_db.sqlite')
cursor = conn.cursor()
for row in cursor.execute("""
SELECT DISTINCT Artist.Name
FROM Artist
JOIN Album ON Artist.ArtistId = Album.ArtistId
JOIN Track ON Album.AlbumId = Track.AlbumId
JOIN Genre ON Track.GenreId = Genre.GenreId
WHERE Genre.Name = ?
ORDER BY Artist.Name
""", (input().strip(),)).fetchall():
    print(row[0])
conn.close()