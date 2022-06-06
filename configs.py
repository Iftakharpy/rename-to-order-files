import re


RECURSIVE_RENAME = False

FILE_EXTENSIONS = ["mp4", "mp3"]
FILE_NUM_REGEX = re.compile(r"^(?P<file_num>\d+).*$")
