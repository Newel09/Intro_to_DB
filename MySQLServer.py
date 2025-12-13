# MySQLServer.py
import os
from mysql.connector import connect, Error

DB_NAME = "alx_book_store"

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD")  # you may replace with env-only if required

def main():
    conn = None
    cursor = None

    try:
        conn = connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        cursor = conn.cursor()

        # No SELECT/SHOW used. Safe if DB already exists.
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`;")
        conn.commit()

        print(f"Database '{DB_NAME}' created successfully!")

    except Error as err:
        print(f"Error: {err}")

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    main()