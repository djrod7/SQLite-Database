import sqlite3

# Connect to a new SQLite database called music.db

connection = sqlite3.connect("music.db")

cursor = connection.cursor()

print("Connected to music.db!")

cursor.execute("PRAGMA foreign_keys = ON")

# Create two tables:
# Artists table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS artists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        genre TEXT
    )
""")

print("Artists table created!")

# Albums table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS albums (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        year INTEGER,
        artist_id INTEGER,
        FOREIGN KEY (artist_id) REFERENCES artists(id)
    )
""")
print("Albums table created!")

# Insert at least 3 artists and 5 albums (make sure some artists have multiple albums)

artists = [
    ("The Kid Laroi", "Hip-Hop"),
    ("Mk.gee", "Alt. R&B"),
    ("Justin Bieber", "Pop")
]

cursor.executemany(
    "INSERT OR IGNORE INTO artists (name, genre) VALUES (?, ?)", artists
)

connection.commit()
print("Artists inserted!")

# Insert 5 albums (make sure some artists have multiple albums)

albums = [
    ("The First Time", 2023, 1),
    ("Before I Forget", 2026, 1),
    ("Two Star & the Dream Police", 2024, 2),
    ("Swag", 2025, 3),
    ("Swag 2", 2025, 3) 
]
cursor.executemany(
    "INSERT OR IGNORE INTO albums (title, year, artist_id) VALUES (?, ?, ?)", albums
)

connection.commit()
print("Albums inserted!")

# Query and print all albums along with a message showing which artist they belong to
cursor.execute("SELECT id, name FROM artists")
artists_rows = cursor.fetchall()

artist_lookup = {}
for row in artists_rows:
    artist_lookup[row[0]] = row[1]

cursor.execute("SELECT title, year, artist_id FROM albums")
album_rows = cursor.fetchall()

print("\nAlbums by artists:")
for row in album_rows:
    title = row[0]
    year = row[1]
    artist_id = row[2]

    artist_name = artist_lookup[artist_id]

    print(f" '{title}' ({year}) by {artist_name}")

# Close the connection
connection.close()
print("\nConnection closed.")

