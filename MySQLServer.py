# MySQLServer.py
import os
import getpass
import mysql.connector

DB_NAME = "alx_book_store"

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")


def main():
    conn = None
    cursor = None

    # Use env var if present; otherwise prompt in terminal (input hidden)
    db_password = os.getenv("DB_PASSWORD")
    if not db_password:
        db_password = getpass.getpass("Enter MySQL password: ")

    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=db_password
        )
        cursor = conn.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
        conn.commit()

        print(f"Database '{DB_NAME}' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == "__main__":
    main()
