import sqlite3

conn = sqlite3.connect('kumo.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    uid TEXT PRIMARY KEY,
    username TEXT NOT NULL,
    name TEXT,
    pfp_url TEXT,
    email TEXT,
    bio TEXT,
    dob TEXT,
    waifu TEXT,
    join_date TEXT,
    location TEXT,
    account_status TEXT,
    social_links TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uid TEXT,
    anime_id INTEGER,
    episode_no INTEGER,
    rating REAL,
    status INTEGER,
    FOREIGN KEY (uid) REFERENCES users (uid)
)
''')


conn.commit()
conn.close()

print("Tables created successfully!")
