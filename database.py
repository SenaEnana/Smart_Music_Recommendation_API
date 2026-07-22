import sqlite3

connection = sqlite3.connect("music-recommendation-database.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS songs (
        id INTEGER PRIMARY KEY,
        title TEXT,
        artist TEXT,
        genre TEXT,
        mood TEXT,
        theme TEXT,
        album TEXT,
        language TEXT,
        explicit No
    )
""")
connection.commit()

#some code here
connection.close()
