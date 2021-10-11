from database.db_connect import DB, CURSOR


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


def get_last_book(fields: Union[str, list[str]] = "All") -> tuple:
    """Retrive the last book added to the database"""
    fields = parse_field_input(fields)
    last_id = get_last_id()
    query = f"SELECT {fields} FROM Book WHERE book_pk = %s"
    CURSOR.execute(query, (last_id,))
    return CURSOR.fetchone()


def get_last_id() -> str:
    last_id = CURSOR.lastrowid
    if last_id != 0:
        return last_id
    CURSOR.execute("SELECT MAX(book_pk) FROM Book")
    return CURSOR.fetchone()[0]


def parse_field_input(field_input: Union[str, list[str]]) -> str:
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
    # To avoid wrong unwanted injections
    if not isinstance(book_id, int):
        raise TypeError(f"Book ID should be int, {type(book_id)} was provided")

    query = f"book_pk = {book_id}"
    remove_book_general(query)


def remove_book_general(delete_condition_query: str) -> None:
    """Remove a book from the DB given a general conditional query"""
    CURSOR.execute("DELETE FROM Book WHERE %s", delete_condition_query)
    DB.commit()
