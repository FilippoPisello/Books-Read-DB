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
