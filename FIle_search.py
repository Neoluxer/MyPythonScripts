# DIRECTORY = r'C:\Users\Professional\Documents\2021\Texts'
DIRECTORY = r"P:\Users\Professional\Documents\2021"
FIND_STRING = 'стандарт'
COUNT_ADDING_SYMBOLS = 30
import os


def find(find_directory, find_string):
    for root, dirs, files in os.walk(find_directory):  # рекурсивная функция
        for name in files:
            find_string_in_file(os.path.join(root, name), find_string)


def find_string_in_file(file, find_string):
    f = open(file, 'r', encoding='utf-8', errors='ignore')
    content = f.read()
    # print(content)
    index = content.find(find_string)
    f.close()
    if index != -1:
        print_find_info(file, content, find_string)


def print_find_info(file, content, find_string):
    index = content.find(find_string)
    start_index = index - COUNT_ADDING_SYMBOLS if index >= COUNT_ADDING_SYMBOLS else 0
    end_index = index + COUNT_ADDING_SYMBOLS + len(find_string)
    content = content[start_index:end_index]
    content = content.replace(find_string, "\x1b[32;1m" + find_string + "\x1b[0m")
    # print (f'{file}:\n...{content[start_index:end_index]}...')
    print()
    print(file)
    print()
    print(content)
    print()


if __name__ == "__main__":
    find(DIRECTORY, FIND_STRING)
