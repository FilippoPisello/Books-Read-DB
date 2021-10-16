from datetime import date

import database.db_actions_general as db_gen
from database.db_connect import CURSOR, DB


############################
# Add bookread
############################
def add_bookread_to_db(
    bookread_id: str,
    book_id: int,
    start_date: date,
    end_date: date,
    days: int,
    score: int = None,
    comment: str = None,
) -> None:
    """Log information about a read book into the DB"""

    content = (book_id, start_date, end_date, days, score, comment, bookread_id)
    addition_query = """
    INSERT INTO Bookread (book_id, start_reading_date, end_reading_date,
    days_passed, out_of_ten_score, comment, bookread_pk)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    CURSOR.execute(addition_query, content)
    DB.commit()


############################
# Delete bookread
############################
def remove_bookread_given_id(bookread_id: str) -> None:
    """Remove a book from the DB given its ID"""
    db_gen.validate_input_type(bookread_id, int)
    query = where_equal_bookreadid(bookread_id)
    remove_bookread_general(query)


def remove_bookread_general(delete_condition_query: str) -> None:
    """Remove a bookread info from the DB given a general conditional query"""
    db_gen.remove_general(CURSOR, DB, "Bookread", delete_condition_query)


############################
# Retrive last bookread
############################
def get_last_bookread(fields: db_gen.FieldsInput = "All") -> tuple:
    """Retrive the last bookread info added to the database"""
    fields = db_gen.parse_field_input(fields)
    last_id = get_last_bookread_id()
    query = f"SELECT {fields} FROM Bookread WHERE book_pk = %s"
    CURSOR.execute(query, (last_id,))
    return CURSOR.fetchone()


def get_last_bookread_id() -> str:
    """Retrive the ID of the last book added in the DB"""
    return db_gen.get_last_id_general(CURSOR, "Bookread", "bookread_pk")


############################
# Conditions for WHERE statements
############################
def where_equal_bookreadid(bookread_id: str) -> str:
    return f"WHERE bookread_pk = {bookread_id}"
