# Поиск вредоносных новых файлов
import os, time
from datetime import datetime
import sys

CHECK_DIR = r"C:\Users\Professional\PycharmProjects"
FILE_LOG = r"C:\Users\Professional\PycharmProjects\RenameFiles\Backup\log.txt"
# TIME_BORDER = 87000   # Кол-во секунд в сутках
TIME_BORDER = 87000   # Кол-во секунд в сутках
DATE_FORMAT = '%d.%m.%Y %H:%M:%S'


def clear_log():
    f = open(FILE_LOG, 'w')
    f.close()


def find_virus(find_directory):
    for root, dirs, files in os.walk(find_directory):  # рекурсивная функция
        for name in files:
            file = os.path.join(root, name)
            if check(file):
                add_to_log(file)


def check(file):
    current_ts = time.time()
    change_time = get_change_time(file)
    return current_ts - change_time < TIME_BORDER


def get_change_time(file):
    m_time = os.stat(file).st_mtime  # Дата модификации
    a_time = os.stat(file).st_atime  # Дата изменения атрибутов
    c_time = os.stat(file).st_ctime  # Дата создания
    return max(m_time, a_time, c_time)


def add_to_log(file):
    adding_string = file + ": " + datetime.fromtimestamp(get_change_time(file)).strftime(DATE_FORMAT) + "\n"
    f = open(FILE_LOG, 'a')  # Добавление в конец файла с сохранением старой информации
    f.write(adding_string)
    print("Finished")
    f.close()


if __name__ == "__main__":
    clear_log()
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        print (directory)
        find_virus(directory)
    else:
        find_virus(CHECK_DIR)
