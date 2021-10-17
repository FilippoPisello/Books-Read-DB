import unittest
from datetime import date

import database.db_actions_books as actbook
import database.db_actions_bookread as actread
from database.db_connect import DB, CURSOR


class TestDBActionsBook(unittest.TestCase):
    """Test the functionalities related to the Book database."""

    def tearDown(self) -> None:
        CURSOR.execute(
            "DELETE FROM Book WHERE title = 'Test'",
        )
        DB.commit()
        CURSOR.reset()

    def test_get_last_book(self):
        """Test whether last book added is correctly retrived"""
        # Add book first
        content = ("Test", "Test xy", "Test", 120, "Test", False, "Test, Test")
        addition_query = """
        INSERT INTO Book (title, author_name, author_surname, pages, genre, owned, tags)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        CURSOR.execute(addition_query, content)
        DB.commit()

        # All fields
        added_book = actbook.get_last_book(fields="All")
        self.assertEqual(added_book[0], "Test")
        self.assertEqual(added_book[1], "Test xy")
        self.assertEqual(added_book[5], False)
        self.assertEqual(added_book[6], "Test, Test")

        # Single field
        added_book = actbook.get_last_book(fields="title")
        self.assertEqual(added_book[0], "Test")
        added_book = actbook.get_last_book(fields="author_name")
        self.assertEqual(added_book[0], "Test xy")

    def test_addbook(self):
        """Test that a book is correctly added to the database"""
        actbook.add_book_to_db("Test", "Test", "Test", 120, "Test", False, "Test, Test")

        added_book = actbook.get_last_book(fields="All")
        self.assertEqual(added_book[0], "Test")
        self.assertEqual(added_book[1], "Test")
        self.assertEqual(added_book[2], "Test")
        self.assertEqual(added_book[3], 120)
        self.assertEqual(added_book[4], "Test")
        self.assertEqual(added_book[5], False)
        self.assertEqual(added_book[6], "Test, Test")

    def test_removebook(self):
        """Test that a book is correctly removed from the database"""
        actbook.add_book_to_db("Test", "edft", "Test", 120, "Test", False, "Test, Test")
        actbook.add_book_to_db(
            "Test", "abcd", "Testtt", 120, "Test", False, "Test, Test"
        )
        actbook.add_book_to_db("Test", "kjim", "Test", 120, "Test", False, "Test, Test")

        last_id = CURSOR.lastrowid
        actbook.remove_book_given_id(last_id)
        name_last = actbook.get_last_book(fields="author_name")

        self.assertEqual(name_last[0], "abcd")

        actbook.remove_book_given_title_author("Test", "abcd", "Testtt")
        name_last = actbook.get_last_book(fields="author_name")
        self.assertEqual(name_last[0], "edft")

    def test_searchbook_id(self):
        """Test that books are correctly searched in the DB using the id"""
        actbook.add_book_to_db("Test", "kjim", "Test", 120, "Test", False, "Test, Test")

        last_id = CURSOR.lastrowid
        search_result = actbook.search_book_given_id(int(last_id))
        self.assertEqual(search_result[1], "kjim")

        # Return None if no book mathces the ID
        search_result = actbook.search_book_given_id(0)
        self.assertIsNone(search_result)

    def test_searchbook_title_author(self):
        actbook.add_book_to_db("Test", "kjim", "Test", 120, "Test", False, "Test, Test")
        last_id = CURSOR.lastrowid
        search_result = actbook.search_book_given_title_author(
            "Test", "kjim", "Test", return_fields="book_pk"
        )
        self.assertEqual(search_result[0], last_id)

        search_result = actbook.search_book_given_title_author(
            "Test", "asjjajajaj", "Test", return_fields="book_pk"
        )
        self.assertIsNone(search_result)

    def test_bookindatabase(self):
        """Test if logical test for book in database works correctly"""
        actbook.add_book_to_db("Test", "kjim", "Test", 120, "Test", False, "Test, Test")

        search1 = actbook.is_book_in_database("Test", "kjim", "Test")
        self.assertTrue(search1)
        search2 = actbook.is_book_in_database("Test", "AShdkhas", "Ahsjhdakhdoah")
        self.assertFalse(search2)

    def test_findbookid(self):
        """Test if book id is correctly retrived given title and author details."""
        actbook.add_book_to_db("Test", "kjim", "Test", 120, "Test", False, "Test, Test")
        last_id = CURSOR.lastrowid

        search_id = actbook.search_bookid_given_title_author("Test", "kjim", "Test")
        self.assertEqual(search_id, last_id)

        search_id = actbook.search_bookid_given_title_author(
            "Ajhasjhdaj", "kjim", "Test"
        )
        self.assertIsNone(search_id)


class TestDBActionsReadbook(unittest.TestCase):
    """Test the functionalities related to the Bookread database."""

    def setUp(self) -> None:
        actbook.add_book_to_db("Test", "Test", "Test", 120, "Test", False, "Test, Test")
        self.id_ = int(actbook.get_last_book_id())

    def tearDown(self) -> None:
        CURSOR.execute(
            "DELETE FROM Bookread WHERE comment = 'Test'",
        )
        CURSOR.execute(
            "DELETE FROM Book WHERE title = 'Test'",
        )
        DB.commit()
        CURSOR.reset()

    def test_get_last_bookread(self):
        """Test whether last bookread added is correctly retrived"""
        # Add book first
        content = (
            self.id_,
            date(2020, 1, 1),
            date(2020, 1, 30),
            30,
            8,
            "Test",
            "1-9012",
        )
        addition_query = """
        INSERT INTO Bookread (book_id, start_reading_date, end_reading_date,
        days_passed, out_of_ten_score, comment, bookread_pk)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        CURSOR.execute(addition_query, content)
        DB.commit()

        # ID
        added_id = actread.get_last_bookread_id()
        self.assertEqual(added_id, "1-9012")

        # All fields
        added_bookread = actread.get_last_bookread(fields="All")
        self.assertEqual(added_bookread[0], self.id_)
        self.assertEqual(added_bookread[1], date(2020, 1, 1))
        self.assertEqual(added_bookread[5], "Test")
        self.assertEqual(added_bookread[6], "1-9012")

        # Single field
        added_bookread = actread.get_last_bookread(fields="out_of_ten_score")
        self.assertEqual(added_bookread[0], 8)
        added_bookread = actread.get_last_bookread(fields="start_reading_date")
        self.assertEqual(added_bookread[0], date(2020, 1, 1))

    def test_addbookread(self):
        """Test that a bookread is correctly added to the database"""
        actread.add_bookread_to_db(
            "1-9012", self.id_, date(2020, 1, 1), date(2020, 1, 30), 30, 8, "Test"
        )

        added_bookread = actread.get_last_bookread(fields="All")
        self.assertEqual(added_bookread[0], self.id_)
        self.assertEqual(added_bookread[1], date(2020, 1, 1))
        self.assertEqual(added_bookread[2], date(2020, 1, 30))
        self.assertEqual(added_bookread[3], 30)
        self.assertEqual(added_bookread[4], 8)
        self.assertEqual(added_bookread[5], "Test")
        self.assertEqual(added_bookread[6], "1-9012")

    def test_removebookread(self):
        """Test that a bookread is correctly removed from the database"""
        actread.add_bookread_to_db(
            "1-9012", self.id_, date(2020, 1, 1), date(2020, 1, 30), 30, 8, "Test"
        )
        actread.add_bookread_to_db(
            "1-9999", self.id_, date(2020, 1, 1), date(2020, 1, 30), 50, 8, "Test"
        )

        actread.remove_bookread_given_id("1-9999")
        days_last = actread.get_last_bookread(fields="days_passed")

        self.assertEqual(days_last[0], 30)


if __name__ == "__main__":
    unittest.main()
