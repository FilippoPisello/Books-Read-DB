import unittest
from datetime import date

from books import Book, BookRead


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
