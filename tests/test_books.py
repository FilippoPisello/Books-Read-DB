import unittest
from datetime import date

from controller.books import Book, BookRead


class TestBooks(unittest.TestCase):
    def setUp(self) -> None:
        self.book1 = Book("Title", "Lorem", "Ipsum", 120, "Genre", False, None)
        self.book2 = Book("title", "lorem", "ipsum", 120, "genre", True, ["Yes", "nO"])

    def test_capitalization(self):
        self.assertEqual(self.book1.title, "Title")
        self.assertEqual(self.book2.title, "Title")

        self.assertEqual(self.book1.author_name, "Lorem")
        self.assertEqual(self.book2.author_name, "Lorem")

        self.assertEqual(self.book1.author_surname, "Ipsum")
        self.assertEqual(self.book2.author_surname, "Ipsum")

        self.assertEqual(self.book1.genre, "Genre")
        self.assertEqual(self.book2.genre, "Genre")

        self.assertIsNone(self.book1.tags)
        self.assertEqual(self.book2.tags, ["yes", "no"])

    def test_ownedint(self):
        self.assertEqual(self.book1.owned, 0)
        self.assertEqual(self.book2.owned, 1)

    def test_author(self):
        self.assertEqual(self.book1.author, "Lorem Ipsum")
        self.assertEqual(self.book2.author, "Lorem Ipsum")

    def test_fromdict(self):
        """Test that Book class instance is correctly created from dict"""
        dict1 = {
            "Book title": "Lorem",
            "Author Name": "Ipsum",
            "Author Surname": "Dolor",
            "Pages": "1",
            "Genre": "Crime",
            "Owned": True,
            "Tags": None,
            "Starting date": "2021-10-18",
            "Ending date": "2021-10-20",
            "Score": "3",
            "Comment": None,
        }
        book1 = Book.from_gui_dict(dict1)
        self.assertEqual(book1.title, "Lorem")
        self.assertEqual(book1.author_name, "Ipsum")
        self.assertEqual(book1.author_surname, "Dolor")
        self.assertEqual(book1.pages, 1)
        self.assertEqual(book1.genre, "Crime")
        self.assertEqual(book1.owned, True)
        self.assertEqual(book1.tags, None)

        dict2 = {
            "Book title": "Lorem",
            "Author Name": "Ipsum",
            "Author Surname": "Dolor",
            "Pages": "1",
            "Genre": "Crime",
            "Owned": True,
            "Tags": "Lorem,Ipsum, Dolor ",
        }
        book2 = Book.from_gui_dict(dict2)
        self.assertEqual(book2.tags, ["lorem", "ipsum", "dolor"])


class TestBookRead(unittest.TestCase):
    def setUp(self) -> None:
        date1 = date(2020, 1, 1)
        date2 = date(2020, 1, 30)
        date3 = date(2020, 2, 15)

        self.read1 = BookRead(1, date1, date2, 8, "Lorem")
        self.read2 = BookRead(2, date2, date3, 1, None)

    def test_bookreadid(self):
        self.assertEqual(self.read1.bookread_id, "1-20200101")
        self.assertEqual(self.read2.bookread_id, "2-20200130")

    def test_daystoread(self):
        self.assertEqual(self.read1.days_to_read, 30)
        self.assertEqual(self.read2.days_to_read, 17)

    def test_fromdict(self):
        """Test that Bookread class instance is correctly created from dict"""
        dict1 = {
            "Book title": "Lorem",
            "Author Name": "Ipsum",
            "Author Surname": "Dolor",
            "Pages": "1",
            "Genre": "Crime",
            "Owned": True,
            "Tags": None,
            "Starting date": "2021-10-18",
            "Ending date": "2021-10-20",
            "Score": "3",
            "Comment": None,
        }
        bookread1 = BookRead.from_gui_dict(dict1, 1)
        self.assertEqual(bookread1.book_id, 1)
        self.assertEqual(bookread1.start_date, date(2021, 10, 18))
        self.assertEqual(bookread1.end_date, date(2021, 10, 20))
        self.assertEqual(bookread1.out_of_ten_score, 3)
        self.assertEqual(bookread1.comment, None)


if __name__ == "__main__":
    unittest.main()
