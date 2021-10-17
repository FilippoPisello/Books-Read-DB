import unittest

from userdata.credentials_reader import DbCredentials
from userdata.booksinfo_reader import BooksInfo


class TestCredentials(unittest.TestCase):
    """Test credentials reading."""

    def test_credentials(self):
        """Test that credentials are correctly read from json file"""
        cred = DbCredentials("tests/testdata/testcredentials.json")
        self.assertEqual(cred.host, "localhost")
        self.assertEqual(cred.username, "FooBar")
        self.assertEqual(cred.password, "BarFoo")


class TestBookinfo(unittest.TestCase):
    """Test bookinfo reading."""

    def test_bookinfo(self):
        """Test that bookinfo are correctly read from json file"""
        info = BooksInfo("tests/testdata/testbookinfo.json")
        self.assertEqual(info.genres, ["Dolor", "Ipsum", "Lorem"])


if __name__ == "__main__":
    unittest.main()
