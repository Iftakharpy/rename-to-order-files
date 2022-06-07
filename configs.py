import re


RECURSIVE_RENAME = False

FILE_EXTENSIONS: list[str] = ["mp4", "mp3", "html", "zip"]
REGEX_FILE_EXTENSIONS: list[re.Pattern] = [re.compile(r"mp\d+")]

FILE_NUM_GROUP_NAME = "file_num"
FILE_NUM_REGEX = re.compile(rf"(?<=^)(?P<{FILE_NUM_GROUP_NAME}>\d+$)(?=.*$)", re.M)
