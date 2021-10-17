"""Read and store book info from dedicated json file"""
import json
from dataclasses import dataclass, field


@dataclass
class BooksInfo:
    """Store the custom book info read from a json file"""

    file_path: str
    genres: list[str] = field(init=False)

    def __post_init__(self):
        self.genres = self.read_info()
        self.genres.sort()

    def read_info(self) -> list[str]:
        """Read the book info from a json file and return the corresponding dict"""
        with open(self.file_path) as file:
            file = json.load(file)

        return file["genres"]


BOOKSINFO = BooksInfo(file_path="userdata/books_info.json")
