import sqlite3
 
conn = sqlite3.connect("mydatabase.db")
 
cursor = conn.cursor()
 
# table creation
cursor.execute("""CREATE TABLE users(id text, name text) """)

conn.commit()
