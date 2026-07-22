import sqlite3

connection = sqlite3.connect("music-recommendation-database.db")
cursor = connection.cursor()

cursor.execute("BEGIN TRANSACTION;")

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
            explicit INTEGER NOT NULL CHECK (explicit IN (0, 1))
        );
    """)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
