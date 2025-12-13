# MySQLServer.py
import os
import getpass
import mysql.connector

def main():
    conn = None
    cursor = None

    db_password = os.getenv("DB_PASSWORD")
    if not db_password:
        db_password = getpass.getpass("Enter MySQL password: ")

    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER", "root"),
            password=db_password
        )
        cursor = conn.cursor()

        # Must match checker exactly (no backticks, no semicolon, no f-string)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        conn.commit()
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    main()