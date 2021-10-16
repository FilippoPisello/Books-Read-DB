from gooey import Gooey, GooeyParser


@Gooey(
    program_name="Book Database",
    program_description="Never lose track of the books you read!",
)
def gui_main() -> dict[str, str]:
    parser = GooeyParser()
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
    )
    book_group.add_argument(
        "Genre",
        choices=["Narrative", "Business/Economics", "Psychology", "Philosophy"],
    )
    book_group.add_argument(
        "--Owned",
        action="store_true",
        help="Click if you own the book",
        default=False,
    )

    args = vars(parser.parse_args())
    print(args)
    return args


if __name__ == "__main__":
    gui_main()
