from typing import Any, Type, Union

FieldsInput = Union[str, list[str]]
SingleresultSearch = Union[tuple[str, ...], None]
MultiresultsSearch = Union[list[tuple[str, ...]], None]

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
