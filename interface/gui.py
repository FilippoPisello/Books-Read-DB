from gooey import Gooey, GooeyParser
from userdata.booksinfo_reader import BOOKSINFO


@Gooey(
    program_name="Book Database",
    program_description="Never lose track of the books you read!",
    default_size=(600, 800),
)
def gui_main() -> dict[str, str]:
    """Render the GUI for the user to provide inputs"""
    parser = GooeyParser()

    add_book_fields(parser)
    add_read_fields(parser)

    args = vars(parser.parse_args())
    print(args)
    return args


def add_book_fields(parser: GooeyParser) -> None:
    """Add the book related fields to the GUI parser"""
    book_group = parser.add_argument_group("Book info")
    book_group.add_argument(
        "Book title",
        gooey_options={"full_width": True},
        help="Add the book title",
    )
    book_group.add_argument(
        "Author Name",
        gooey_options={"full_width": False},
        help="Add the name of the author",
    )
    book_group.add_argument(
        "Author Surname",
        gooey_options={"full_width": False},
        help="Add the surname of the author",
    )
    book_group.add_argument(
        "-Pages",
        "--Pages",
        help="Add the number of pages",
        widget="IntegerField",
        gooey_options={"min": 1, "max": 10000},
    )
    book_group.add_argument(
        "Genre",
        choices=BOOKSINFO.genres,
    )
    book_group.add_argument(
        "--Owned",
        action="store_true",
        help="Click if you own the book",
        default=False,
    )
    book_group.add_argument(
        "--Tags",
        help="Add some comma-separated tags",
    )


def add_read_fields(parser: GooeyParser) -> None:
    """Add the read related fields to the GUI parser"""
    read_group = parser.add_argument_group("Reading info")
    read_group.add_argument(
        "Starting date",
        help="Pick the date when you started reading the book",
        widget="DateChooser",
    )
    read_group.add_argument(
        "Ending date",
        help="Pick the date when you finished the book",
        widget="DateChooser",
    )
    read_group.add_argument(
        "--Score",
        help="Choose a score from 0 to 10",
        gooey_options={"min": 0, "max": 10},
        widget="Slider",
        default=None,
    )
    read_group.add_argument(
        "--Comment",
        help="Add a comment on the book",
        default=None,
    )


if __name__ == "__main__":
    gui_main()
