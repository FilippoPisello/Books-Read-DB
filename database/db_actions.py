from typing import Type, Union, Any
from database.db_connect import DB, CURSOR

FieldsInput = Union[str, list[str]]
SingleresultSearch = Union[tuple[str, ...], None]
MultiresultsSearch = Union[tuple[tuple[str, ...], ...], None]


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


def get_last_book(fields: FieldsInput = "All") -> tuple:
    """Retrive the last book added to the database"""
    fields = parse_field_input(fields)
    last_id = get_last_id()
    query = f"SELECT {fields} FROM Book WHERE book_pk = %s"
    CURSOR.execute(query, (last_id,))
    return CURSOR.fetchone()


def get_last_id() -> str:
    """Retrive the ID of the last book added in the DB"""
    last_id = CURSOR.lastrowid
    if last_id != 0:
        return last_id
    CURSOR.execute("SELECT MAX(book_pk) FROM Book")
    return CURSOR.fetchone()[0]


def parse_field_input(field_input: FieldsInput) -> str:
    """Transform an indication of field into str to be passed to query"""
    if field_input == "All":
        return "*"
    if isinstance(field_input, list):
        return " ".join(field_input)
    if isinstance(field_input, str):
        return field_input
    raise TypeError(
        f"Field input should be str or list, {type(field_input)} was provided."
    )


def remove_book_given_id(book_id: int) -> None:
    """Remove a book from the DB given its ID"""
    validate_input_type(book_id, int)

    query = f"book_pk = {book_id}"
    remove_book_general(query)


def remove_book_given_title_author(
    title: str, author_name: str, author_surname: str
) -> None:
    """Remove a book from the DB given its ID"""
    for arg in [title, author_name, author_surname]:
        validate_input_type(arg, str)

    query = f"""title = '{title}'
    AND author_name = '{author_name}'
    AND author_surname = '{author_surname}'"""
    remove_book_general(query)


def remove_book_general(delete_condition_query: str) -> None:
    """Remove a book from the DB given a general conditional query"""
    CURSOR.execute(f"DELETE FROM Book WHERE {delete_condition_query}")
    DB.commit()


def validate_input_type(input_item: Any, exp_type: Type) -> None:
    """To avoid unwanted injections, raise an error if input_item is not of type
    exp_type"""
    if not isinstance(input_item, exp_type):
        raise TypeError(
            f"Book ID should be {exp_type}, {type(input_item)} was provided"
        )


def search_book_given_title_author(
    title: str, author_name: str, author_surname: str, fields: FieldsInput = "All"
) -> MultiresultsSearch:
    """Remove a book from the DB given its ID"""
    for arg in [title, author_name, author_surname]:
        validate_input_type(arg, str)

    query = f"""title = '{title}'
    AND author_name = '{author_name}'
    AND author_surname = '{author_surname}'"""
    return search_book_general(query, fields)


def search_book_given_id(
    book_id: int, fields: FieldsInput = "All"
) -> SingleresultSearch:
    """Search a book by id in the database. Return info as a tuple if found,
    None otherwise."""
    validate_input_type(book_id, int)

    query = f"book_pk = {book_id}"
    return search_book_general(query, fields, return_one=True)


def search_book_general(
    search_condition_query: str, fields: FieldsInput = "All", return_one=False
) -> Union[MultiresultsSearch, SingleresultSearch]:
    """Run a search in the database and return the results. If return_one, only
    last result is returned."""
    fields = parse_field_input(fields)
    CURSOR.execute(f"SELECT {fields} FROM Book WHERE {search_condition_query}")
    if return_one:
        return CURSOR.fetchone()
    return CURSOR.fetchall()
