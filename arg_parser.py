import argparse
import configs

from arg_converters import (
    convert_to_path,
    convert_to_regular_expression,
)


DESCRIPTION = """
    Simple script to rename files. Target is to find the files which has number in file name and 
    replace the numbers in file name to make number same length. For example a list of file names 
    ['1. lesson.mp4', '2. lesson.mp4', ..., '100. lesson.mp4'] would be renamed to 
    ['001. lesson.mp4', '002. lesson.mp4', ..., '100. lesson.mp4'] to match the length of the 
    biggest number of same file extension.
    """

arg_parser = argparse.ArgumentParser(description=DESCRIPTION)
arg_parser.add_argument("path", type=convert_to_path, help="Path to the parent folder")
arg_parser.add_argument(
    "-fx",
    "--file_extensions",
    nargs="*",
    type=str,
    default=configs.FILE_EXTENSIONS,
    help=f"Files to rename having extensions. Default: {configs.FILE_EXTENSIONS}",
)
arg_parser.add_argument(
    "-r",
    "--recursive",
    default=configs.RECURSIVE_RENAME,
    action="store_true",
    help="Recursively rename files",
)
arg_parser.add_argument(
    "-fnr",
    "--file_num_regex",
    type=convert_to_regular_expression,
    default=configs.FILE_NUM_REGEX,
    help=f"Regular expression to find file name. Default: '{configs.FILE_NUM_REGEX.pattern}'",
)

parsed_args = arg_parser.parse_args()
