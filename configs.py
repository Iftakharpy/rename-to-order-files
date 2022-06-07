import re


RECURSIVE_RENAME = False

FILE_EXTENSIONS = ["mp4", "mp3"]

FILE_NUM_GROUP_NAME = "file_num"
FILE_NUM_REGEX = re.compile(rf"(?<=^)(?P<{FILE_NUM_GROUP_NAME}>\d+)(?=.*$)", re.M)
