from typing import Union
from database.db_connect import DB, CURSOR
import database.db_actions_general as db_gen


############################
# Add book
############################
def add_book_to_db(
    title: str,
    author_name: str,
    author_surname: str,
    pages: int,
    genre: str,
    owned: bool = None,
    tags: str = None,
) -> None:
    """Log a book into the DB"""

    content = (title, author_name, author_surname, pages, genre, owned, tags)
    addition_query = """
    INSERT INTO Book (title, author_name, author_surname, pages, genre, owned, tags)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    CURSOR.execute(addition_query, content)
    DB.commit()


############################
# Delete book
############################
def remove_book_given_id(book_id: int) -> None:
    """Remove a book from the DB given its ID"""
    db_gen.validate_input_type(book_id, int)
    query = where_equal_bookid(book_id)
    remove_book_general(query)


def remove_book_given_title_author(
    title: str, author_name: str, author_surname: str
) -> None:
    """Remove a book from the DB given its ID"""
    db_gen.validate_multiple_inputs_type([title, author_name, author_surname], str)
    query = where_equal_title_author(title, author_name, author_surname)
    remove_book_general(query)


def remove_book_general(delete_condition_query: str) -> None:
    """Remove a book from the DB given a general conditional query"""
    db_gen.remove_general(CURSOR, DB, "Book", delete_condition_query)


############################
# Retrive last book
############################
def get_last_book(fields: db_gen.FieldsInput = "All") -> tuple:
    """Retrive the last book added to the database"""
    fields = db_gen.parse_field_input(fields)
    last_id = get_last_book_id()
    query = f"SELECT {fields} FROM Book WHERE book_pk = %s"
    CURSOR.execute(query, (last_id,))
    return CURSOR.fetchone()


def get_last_book_id() -> str:
    """Retrive the ID of the last book added in the DB"""
    return db_gen.get_last_id_general(CURSOR, "Book", "book_pk")


############################
# Search book
############################
def is_book_in_database(title: str, author_name: str, author_surname: str) -> bool:
    """Return True if search criteria meet at least a book in the DB, False
    otherwise."""
    return bool(search_book_given_title_author(title, author_name, author_surname))


def search_bookid_given_title_author(
    title: str, author_name: str, author_surname: str
) -> Union[str, None]:
    """Return book id given title and author details."""
    res = search_book_given_title_author(title, author_name, author_surname, "book_pk")
    if res:
        return res[0]
    return None


def search_book_given_title_author(
    title: str,
    author_name: str,
    author_surname: str,
    return_fields: db_gen.FieldsInput = "All",
) -> db_gen.MultiresultsSearch:
    """Search a book by title and author in the database. Return info as a
    tuple if found, None otherwise."""
    db_gen.validate_multiple_inputs_type([title, author_name, author_surname], str)
    query = where_equal_title_author(title, author_name, author_surname)
    return search_book_general(query, return_fields, return_one=True)


def search_book_given_id(
    book_id: int, return_fields: db_gen.FieldsInput = "All"
) -> db_gen.SingleresultSearch:
    """Search a book by id in the database. Return info as a tuple if found,
    None otherwise."""
    db_gen.validate_input_type(book_id, int)
    query = where_equal_bookid(book_id)
    return search_book_general(query, return_fields, return_one=True)


def search_book_general(
    search_condition_query: str,
    return_fields: db_gen.FieldsInput = "All",
    return_one=False,
) -> Union[db_gen.MultiresultsSearch, db_gen.SingleresultSearch]:
    """Run a search in the database and return the results. If return_one, only
    last result is returned."""
    return db_gen.search_general(
        CURSOR, "Book", search_condition_query, return_fields, return_one
    )


############################
# Conditions for WHERE statements
############################
def where_equal_bookid(book_id: int) -> str:
    return f"WHERE book_pk = {book_id}"


def where_equal_title_author(title: str, author_name: str, author_surname: str) -> str:
    query = f"""WHERE
    title = '{title}'
    AND author_name = '{author_name}'
    AND author_surname = '{author_surname}'"""
    return query

############################
# Other
############################
def reset_pk_book():
    db_gen.reset_pd_general(CURSOR, "Book", "book_pk")