try:
    import mysql.connector
except ModuleNotFoundError:
    raise SystemExit("Missing package: run `python -m pip install mysql-connector-python` to install it.")

from calendar import Error
import os

# Prefer reading credentials from environment variables
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "14523512Newel")
DB_NAME = os.getenv("DB_NAME", "university_system")

conn = None
try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    if conn.is_connected():
        print("Connected to MySQL server version", conn.get_server_info())
except Error as e:
    print("Error connecting to MySQL:", e)
finally:
    if conn and conn.is_connected():
        conn.close()