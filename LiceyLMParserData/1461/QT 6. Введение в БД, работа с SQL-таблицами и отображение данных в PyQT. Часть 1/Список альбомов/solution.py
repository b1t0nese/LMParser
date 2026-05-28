import sqlite3

cur = sqlite3.connect("music_db.sqlite").cursor()
alboms = map(lambda x: x[0], cur.execute("""SELECT DISTINCT Album.Title FROM Album
JOIN Track ON Album.AlbumId = Track.AlbumId
JOIN Genre ON Track.GenreId = Genre.GenreId
WHERE Genre.Name = ?
ORDER BY Album.ArtistId, Album.Title;""", (input(),)).fetchall())
print("\n".join(alboms))