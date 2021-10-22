import os
from transliterate import translit, get_available_language_codes
import sys

DIRECTORY = 'C:\\Users\\Professional\\Pictures\\for_site'


def rename_files(find_directory):
    for root, dirs, files in os.walk(find_directory):  # рекурсивная функция
        for name in files:
            rename_file(root, name)


def rename_file(root, name):
    valid_name = get_valid_name(name)
    old_file = os.path.join(root, name)
    new_file = os.path.join(root, valid_name)
    os.rename(old_file,new_file)


def get_valid_name(name):
    name = name.replace(" ", "_")
    name = name.lower()
    text = name
    name = (translit(text, 'ru', reversed=True))
    return name


if __name__ == '__main__':
    rename_files(DIRECTORY)
