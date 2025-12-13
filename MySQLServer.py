import os
from mysql.connector import connect, Error

DB_NAME = os.getenv("DB_NAME", "alx_book_store")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD")  # do not hardcode

def main():
    if not DB_PASSWORD:
        raise ValueError("DB_PASSWORD is not set in environment variables.")

    try:
        with connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`;")
            conn.commit()
            print(f"Database '{DB_NAME}' created successfully!")
    except Error as err:
        print(f"MySQL Error: {err}")

if __name__ == "__main__":
    main()