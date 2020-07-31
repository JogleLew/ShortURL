import sqlite3
conn = sqlite3.connect("shorturl.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE url (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        shorten   text,
        expand    text
    );
    """
)
conn.commit()
conn.close()
