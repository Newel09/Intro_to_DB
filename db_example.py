import os
from mysql.connector import connect, Error
# Prefer reading credentials from environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "university_system")

conn = None
try:
    conn = connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
        )
    
except Error as e:
    print("Error connecting to MySQL:", e)
finally:
    if conn and conn.is_connected():
        conn.close()