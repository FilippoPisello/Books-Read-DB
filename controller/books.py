from dataclasses import dataclass
from datetime import date
from typing import Union


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
            self.tags = [tag.lower().strip() for tag in self.tags]

    def __eq__(self, other):
        return (self.title == other.title) & (self.author == other.author)

    @classmethod
    def from_gui_dict(cls, gui_dict: dict[str, Union[str, bool, None]]):
        title = gui_dict["Book title"]
        name = gui_dict["Author Name"]
        surname = gui_dict["Author Surname"]
        pages = int(gui_dict["Pages"])
        genre = gui_dict["Genre"]
        owned = gui_dict["Owned"]
        tags = None if gui_dict["Tags"] is None else gui_dict["Tags"].split(",")
        return cls(title, name, surname, pages, genre, owned, tags)


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

    @classmethod
    def from_gui_dict(cls, gui_dict: dict[str, Union[str, bool, None]], book_id: int):
        start_date = cls.str_date_to_date(gui_dict["Starting date"])
        end_date = cls.str_date_to_date(gui_dict["Ending date"])
        out_of_ten_score = int(gui_dict["Score"])
        comment = gui_dict["Comment"]
        return cls(book_id, start_date, end_date, out_of_ten_score, comment)

    @staticmethod
    def str_date_to_date(str_date: str) -> date:
        """Transform a date passed as str in the form 'YYYY-MM-DD' to
        proper datetime.date type."""
        date_items: list[str, str, str] = str_date.split("-")
        date_items = [int(x) for x in date_items]
        year, month, day = date_items
        return date(year, month, day)
