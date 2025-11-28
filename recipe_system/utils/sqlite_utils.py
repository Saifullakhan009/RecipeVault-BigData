import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("interactions.db", check_same_thread=False)
cursor = conn.cursor()

# Initialize the table
def initialize_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interactions (
        recipe_id TEXT PRIMARY KEY,
        action TEXT
    )
    """)
    conn.commit()

# Log an interaction
def log_interaction(recipe_id, action):
    cursor.execute("""
    INSERT OR REPLACE INTO interactions (recipe_id, action) VALUES (?, ?)
    """, (recipe_id, action))
    conn.commit()

# Get interaction by recipe_id
def get_interaction(recipe_id):
    cursor.execute("""
    SELECT * FROM interactions WHERE recipe_id = ?
    """, (recipe_id,))
    return cursor.fetchone()

# Initialize table when module is imported
initialize_table()
