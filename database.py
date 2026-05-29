import sqlite3

# Connect database
conn = sqlite3.connect(
    "career_history.db",
    check_same_thread=False
)

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    skills TEXT,

    interests TEXT,

    personality TEXT,

    careers TEXT
)
""")

conn.commit()


# Save recommendation
def save_recommendation(
    skills,
    interests,
    personality,
    careers
):

    careers_text = ", ".join(careers)

    cursor.execute("""
    INSERT INTO history (
        skills,
        interests,
        personality,
        careers
    )

    VALUES (?, ?, ?, ?)
    """, (
        skills,
        interests,
        personality,
        careers_text
    ))

    conn.commit()


# Fetch history
def get_history():

    cursor.execute("""
    SELECT * FROM history
    ORDER BY id DESC
    """)

    return cursor.fetchall()