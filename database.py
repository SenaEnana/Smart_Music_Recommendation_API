import sqlite3

DB_NAME = "music-recommendation-database.db"

def init_db():
    """Run this once to make sure the table exists."""
    connection = sqlite3.connect(DB_NAME)
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
    connection.commit()
    connection.close()

