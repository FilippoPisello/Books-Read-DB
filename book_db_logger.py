"""Run the interface, pass the info to the DB and store the info"""

from interface.gui import gui_main
from controller.books import Book, BookRead
import database.db_actions_books as db_book
import database.db_actions_bookread as db_read


def main():
    user_input = gui_main()

    book = Book.from_gui_dict(user_input)

    if db_book.is_book_in_database(book.title, book.author_name, book.author_surname):
        book_id = db_book.search_bookid_given_title_author(
            book.title, book.author_name, book.author_surname
        )
        print("The book was already in the database so it was not added again.")

    else:
        db_book.add_book_to_db(
            title=book.title,
            author_name=book.author_name,
            author_surname=book.author_surname,
            pages=book.pages,
            genre=book.genre,
            owned=book.owned,
            tags=book.string_tags,
        )
        book_id = db_book.get_last_book_id()
        print("Book correctly added in the database!")

    book_id = int(book_id)
    bookread = BookRead.from_gui_dict(user_input, book_id)
    db_read.add_bookread_to_db(
        bookread_id=bookread.bookread_id,
        book_id=bookread.book_id,
        start_date=bookread.start_date,
        end_date=bookread.end_date,
        days=bookread.days_to_read,
        score=bookread.out_of_ten_score,
        comment=bookread.comment,
    )
    print("Book read info correctly added in the database!")
    print("Process compelted successfull!\n\n\n")

if __name__ == "__main__":
    main()
