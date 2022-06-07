import re
from pathlib import Path

import configs
from arg_parser import parsed_args


def get_file_number(
    file_path: Path,
    file_num_regex: re.Pattern = parsed_args.file_num_regex,
    file_num_group_name: re.Match = configs.FILE_NUM_GROUP_NAME,
) -> int:
    # Find file number from file name
    match = file_num_regex.search(file_path.name)
    if not match:
        raise ValueError("File path does not contain a number")

    # Prepare new file number to replace old file number
    file_num = int(match.group(file_num_group_name))
    return file_num


def get_file_path(
    file_path: Path,
    max_file_number: int,
    fill_char="0",
    file_num_regex: re.Pattern = parsed_args.file_num_regex,
) -> Path:
    length = len(str(max_file_number))

    # Prepare new file number to replace old file number
    try:
        file_num = get_file_number(file_path)
        new_file_num = f"{file_num:{fill_char}{length}d}"
    except ValueError:
        print("Did not find a match for file: ", file_path)
        return file_path

    # Prepare new file path
    new_file_name = file_num_regex.subn(new_file_num, file_path.name, 1)[0]
    new_file_path = file_path.parent / new_file_name
    return new_file_path


def filter_and_rename_files(
    parent_path: Path = parsed_args.path,
    is_recursive: bool = parsed_args.recursive,
    file_extensions: set[str] = set(parsed_args.file_extensions),
    regex_file_extensions: list[re.Pattern] = configs.REGEX_FILE_EXTENSIONS,
) -> None:
    max_file_number = 0
    files_to_rename: list[Path] = []

    for path in parent_path.iterdir():
        if path.is_dir() and is_recursive:
            # Recurse when path is a directory and is_recursive is True
            filter_and_rename_files(
                parent_path=path,
                file_extensions=file_extensions,
                is_recursive=is_recursive,
            )
            continue

        if path.is_file():
            try:
                file_num = get_file_number(path)

                extensions = path.suffixes
                for extension in extensions:
                    is_rename_candidate = False

                    extension = extension[1:]
                    if extension in file_extensions:
                        is_rename_candidate = True
                    else:
                        for regexp in regex_file_extensions:
                            match = regexp.search(extension)
                            if match:
                                is_rename_candidate = True
                                break

                    if is_rename_candidate:
                        # Add path to rename candidate when file
                        # extension is in specified file extensions
                        files_to_rename.append(path)
                        max_file_number = max(file_num, max_file_number)
                        break
            except ValueError:
                pass

    for file in files_to_rename:
        new_file_path = get_file_path(file, max_file_number)
        print(file.name, "->", new_file_path.name)
        file.rename(new_file_path)


def main():
    filter_and_rename_files()


if __name__ == "__main__":
    main()
