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

    def test_addbook(self):
        """Test that a book is correctly added to the database"""
        act.add_book_to_db("Test", "Test", "Test", 120, "Test", False, "Test, Test")

        last_id = CURSOR.lastrowid
        select_query = "SELECT * FROM Book WHERE book_pk = %s"
        CURSOR.execute(select_query, (last_id,))
        added_book = CURSOR.fetchone()

        self.assertEqual(added_book[0], "Test")
        self.assertEqual(added_book[1], "Test")
        self.assertEqual(added_book[2], "Test")
        self.assertEqual(added_book[3], 120)
        self.assertEqual(added_book[4], "Test")
        self.assertEqual(added_book[5], False)
        self.assertEqual(added_book[6], "Test, Test")


if __name__ == "__main__":
    unittest.main()
