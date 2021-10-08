from mysql.connector import Error as db_error

from database.db_connect import GENERAL_CURSOR, CURSOR

try:
    GENERAL_CURSOR.execute("CREATE DATABASE books_database")
except db_error as err:
    if err.errno == 1007:
        print("The database already exists, no action is taken.")
    else:
        raise err

book_table_creation_q = """
    CREATE TABLE Book (
        title VARCHAR(70) NOT NULL,
        author_name VARCHAR(50) NOT NULL,
        author_surname VARCHAR(50) NOT NULL,
        pages SMALLINT UNSIGNED NOT NULL,
        genre VARCHAR(30) NOT NULL,
        owned TINYINT UNSIGNED NOT NULL,
        tags VARCHAR(50),
        book_pk INT UNSIGNED PRIMARY KEY AUTO_INCREMENT)
"""

bookread_table_creation_q = """
    CREATE TABLE BookRead (
        book_id INT UNSIGNED NOT NULL, FOREIGN KEY(book_id) REFERENCES Book(book_pk),
        start_reading_date DATE NOT NULL,
        end_reading_date DATE NOT NULL,
        days_passed SMALLINT UNSIGNED,
        out_of_ten_score TINYINT UNSIGNED,
        comment VARCHAR(300),
        bookread_pk VARCHAR(20) PRIMARY KEY)
"""

CURSOR.execute(book_table_creation_q)
CURSOR.execute(bookread_table_creation_q)
