import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name,
        surname,
        last_name,
        email,
        age)
""")
conn.commit()
conn.close()
