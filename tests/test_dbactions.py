import unittest

import database.db_actions as act
from database.db_connect import DB, CURSOR


class TestDBActions(unittest.TestCase):
    """Test the functionalities related to the database."""

    def tearDown(self) -> None:
        CURSOR.execute(
            "DELETE FROM Book WHERE title = 'Test'",
        )
        DB.commit()

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
        added_book = act.get_last_book(fields="All")
        self.assertEqual(added_book[0], "Test")
        self.assertEqual(added_book[1], "Test xy")
        self.assertEqual(added_book[5], False)
        self.assertEqual(added_book[6], "Test, Test")

        # Single field
        added_book = act.get_last_book(fields="title")
        self.assertEqual(added_book[0], "Test")
        added_book = act.get_last_book(fields="author_name")
        self.assertEqual(added_book[0], "Test xy")

    def test_addbook(self):
        """Test that a book is correctly added to the database"""
        act.add_book_to_db("Test", "Test", "Test", 120, "Test", False, "Test, Test")

        added_book = act.get_last_book(fields="All")
        self.assertEqual(added_book[0], "Test")
        self.assertEqual(added_book[1], "Test")
        self.assertEqual(added_book[2], "Test")
        self.assertEqual(added_book[3], 120)
        self.assertEqual(added_book[4], "Test")
        self.assertEqual(added_book[5], False)
        self.assertEqual(added_book[6], "Test, Test")

    def test_removebook(self):
        """Test that a book is correctly removed from the database"""
        act.add_book_to_db("Test", "edft", "Test", 120, "Test", False, "Test, Test")
        act.add_book_to_db("Test", "abcd", "Testtt", 120, "Test", False, "Test, Test")
        act.add_book_to_db("Test", "kjim", "Test", 120, "Test", False, "Test, Test")

        last_id = CURSOR.lastrowid
        act.remove_book_given_id(last_id)
        name_last = act.get_last_book(fields="author_name")

        self.assertEqual(name_last[0], "abcd")

        act.remove_book_given_title_author("Test", "abcd", "Testtt")
        name_last = act.get_last_book(fields="author_name")
        self.assertEqual(name_last[0], "edft")

    def test_searchbook_id(self):
        """Test that books are correctly searched in the DB using the id"""
        act.add_book_to_db("Test", "kjim", "Test", 120, "Test", False, "Test, Test")

        last_id = CURSOR.lastrowid
        search_result = act.search_book_given_id(int(last_id))
        self.assertEqual(search_result[1], "kjim")

        # Return None if no book mathces the ID
        search_result = act.search_book_given_id(0)
        self.assertIsNone(search_result)

    def test_searchbook_title_author(self):
        act.add_book_to_db("Test", "kjim", "Test", 120, "Test", False, "Test, Test")
        last_id = CURSOR.lastrowid
        search_result = act.search_book_given_title_author(
            "Test", "kjim", "Test", return_fields="book_pk"
        )
        self.assertEqual(search_result[0], last_id)

        search_result = act.search_book_given_title_author(
            "Test", "asjjajajaj", "Test", return_fields="book_pk"
        )
        self.assertIsNone(search_result)

    def test_bookindatabase(self):
        """Test if logical test for book in database works correctly"""
        act.add_book_to_db("Test", "kjim", "Test", 120, "Test", False, "Test, Test")

        search1 = act.is_book_in_database("Test", "kjim", "Test")
        self.assertTrue(search1)
        search2 = act.is_book_in_database("Test", "AShdkhas", "Ahsjhdakhdoah")
        self.assertFalse(search2)

    def test_findbookid(self):
        """Test if book id is correctly retrived given title and author details."""
        act.add_book_to_db("Test", "kjim", "Test", 120, "Test", False, "Test, Test")
        last_id = CURSOR.lastrowid

        search_id = act.search_bookid_given_title_author("Test", "kjim", "Test")
        self.assertEqual(search_id, last_id)

        search_id = act.search_bookid_given_title_author("Ajhasjhdaj", "kjim", "Test")
        self.assertIsNone(search_id)


if __name__ == "__main__":
    unittest.main()
