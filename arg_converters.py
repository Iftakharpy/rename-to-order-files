import re
from pathlib import Path


def convert_to_path(path: str):
    path = Path(path)
    if path.is_dir():
        return path
    raise ValueError("File path do not exist.")


def convert_to_regular_expression(regular_expression: str):
    try:
        regular_expression = re.compile(regular_expression)
        return regular_expression
    except Exception as e:
        print("Regex pattern: ", e)
        raise ValueError("Invalid regex pattern")


def convert_list_to_set(file_paths: list[str]):
    return set(file_paths)
