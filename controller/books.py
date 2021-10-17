from dataclasses import dataclass
from datetime import date


@dataclass
class Book:
    """Class to represent a book with its features."""

    title: str
    author_name: str
    author_surname: str
    pages: int
    genre: str
    owned: bool = None
    tags: list[str] = None

    @property
    def author(self):
        """Return author name and surname"""
        return self.author_name + " " + self.author_surname

    def __post_init__(self):
        """Standardize inputs when object is created passed."""
        self.title = self.title.title()
        self.author_name = self.author_name.title()
        self.author_surname = self.author_surname.title()
        self.genre = self.genre.title()
        self.owned = int(self.owned)

        if self.tags is not None:

    def __eq__(self, other):
        return (self.title == other.title) & (self.author == other.author)


@dataclass
class BookRead:
    """Class to represent the information about a read book."""

    book_id: int
    start_date: date
    end_date: date
    out_of_ten_score: int = None
    comment: str = None

    @property
    def bookread_id(self):
        return str(self.book_id) + "-" + str(self.start_date).replace("-", "")

    @property
    def days_to_read(self):
        return (self.end_date - self.start_date).days + 1

    def __eq__(self, other):
        return (self.book_id == other.book_id) & (self.start_date == other.start_date)
