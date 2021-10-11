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
        act.add_book_to_db("Test", "abcd", "Test", 120, "Test", False, "Test, Test")
        act.add_book_to_db("Test", "kjim", "Test", 120, "Test", False, "Test, Test")

        last_id = CURSOR.lastrowid
        act.remove_book_given_id(last_id)
        name = act.get_last_book(fields="author_name")

        self.assertEqual(name[0], "abcd")


if __name__ == "__main__":
    unittest.main()
