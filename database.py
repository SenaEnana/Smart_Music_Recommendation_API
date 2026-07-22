import sqlite3

connection = sqlite3.connect("music-recommendation-database.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS songs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        artist TEXT,
        genre TEXT,
        mood TEXT,
        theme TEXT,
        album TEXT,
        language TEXT,
        explicit INTEGER NOT NULL CHECK (explicit IN (0, 1))
    );
""")

single_song = ("The Search", "NF", "Rap", "Calm", "Self Reflection", "The Search", "English", 0)
cursor.execute(
    """
    INSERT INTO songs (title, artist, genre, mood, theme, album, language, explicit) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, 
    single_song
)

cursor.execute("SELECT * FROM songs")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.commit()

