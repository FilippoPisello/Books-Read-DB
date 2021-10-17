from typing import Any, Type, Union

FieldsInput = Union[str, list[str]]
SingleresultSearch = Union[tuple[str, ...], None]
MultiresultsSearch = Union[list[tuple[str, ...]], None]

################################################################################
# General Actions
################################################################################
def get_last_id_general(cursor, table_name: str, pk_name: str) -> str:
    """Retrive the ID of the last item added in the DB."""
    last_id = cursor.lastrowid
    if last_id != 0:
        return last_id
    cursor.execute(f"SELECT MAX({pk_name}) FROM {table_name} LIMIT 0, 1")
    return cursor.fetchone()[0]


def remove_general(cursor, db, table_name: str, delete_condition_query: str) -> None:
    """Remove an item from the DB given a general conditional query."""
    cursor.execute(f"DELETE FROM {table_name} {delete_condition_query}")
    db.commit()


def search_general(
    cursor,
    table_name: str,
    search_condition_query: str,
    return_fields: FieldsInput = "All",
    return_one=False,
) -> Union[MultiresultsSearch, SingleresultSearch]:
    """Run a search in the database and return the results. If return_one, only
    last result is returned."""
    return_fields = parse_field_input(return_fields)

    multi_query = f"SELECT {return_fields} FROM {table_name} {search_condition_query}"

    # Get one result if just one is needed
    if return_one:
        single_query = multi_query + " LIMIT 0, 1"
        cursor.execute(single_query)
        return cursor.fetchone()

    # Get all the results
    cursor.execute(multi_query)
    multiple_result = cursor.fetchall()
    # For consistency, if no result then return None
    return multiple_result if multiple_result else None


################################################################################
# Utilities
################################################################################
def parse_field_input(field_input: FieldsInput) -> str:
    """Transform an indication of field into str to be passed to query"""
    if field_input == "All":
        return "*"
    if isinstance(field_input, list):
        return " ".join(field_input)
    if isinstance(field_input, str):
        return field_input
    raise TypeError(
        f"Field input should be str or list, {type(field_input)} was provided."
    )


def validate_multiple_inputs_type(input_items_list: list[Any], exp_type: Type) -> None:
    """Raise an error if each item in input_items_list is not of type exp_type"""
    for item in input_items_list:
        validate_input_type(item, exp_type)


def validate_input_type(input_item: Any, exp_type: Type) -> None:
    """Raise an error if input_item is not of type exp_type"""
    if not isinstance(input_item, exp_type):
        raise TypeError(
            f"Book ID should be {exp_type}, {type(input_item)} was provided"
        )
