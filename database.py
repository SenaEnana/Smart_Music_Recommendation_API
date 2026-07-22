import sqlite3

connection = sqlite3.connect("music-recommendation-database.db")
cursor = connection.cursor()

cursor.execute("BEGIN TRANSACTION;")

try:
    # 3. Create the new table with the corrected schema and CHECK constraint
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS songs_new (
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

    # 4. Copy data from the old table to the new table
    cursor.execute("""
        INSERT INTO songs_new (id, title, artist, genre, mood, theme, album, language, explicit)
        SELECT id, title, artist, genre, mood, theme, album, language, explicit 
        FROM songs;
    """)

    # 5. Drop the old table
    cursor.execute("DROP TABLE songs;")

    # 6. Rename the new table to the original table name
    cursor.execute("ALTER TABLE songs_new RENAME TO songs;")
    
    connection.commit()
    print("Table successfully updated to the new schema!")

except sqlite3.Error as e:
    # Rollback changes if anything goes wrong to protect your data
    connection.rollback()
    print(f"An error occurred during migration: {e}")

finally:
    # 8. Always close the connection
    connection.close()
