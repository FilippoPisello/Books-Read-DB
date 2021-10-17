import unittest

from userdata.credentials_reader import DbCredentials


class TestCredentials(unittest.TestCase):
    """Test credentials reading."""

    def test_credentials(self):
        """Test that credentials are correctly read from json file"""
        cred = DbCredentials("tests/testdata/testcredentials.json")
        self.assertEqual(cred.host, "localhost")
        self.assertEqual(cred.username, "FooBar")
        self.assertEqual(cred.password, "BarFoo")


if __name__ == "__main__":
    unittest.main()
