import sqlite3
conn = sqlite3.connect("jobs_database.db")
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE jobs (
        job_id INTEGER PRIMARY KEY,
        title TEXT,
        url TEXT,
        location TEXT,
        department TEXT
    );
    """
)
conn.commit()
conn.close()
