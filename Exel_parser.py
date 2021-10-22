
import xlrd3 as xlrd

FILE = 'Test.xls'


def parsing(file):
    book = xlrd.open_workbook(file)
    sh = book.sheet_by_index(0)
    for row_number in range(sh.nrows):
        for col_number in range(sh.ncols):
            print(sh.cell_value(rowx=row_number, colx=col_number))


def do(file):
    articles = []
    expenses = []
    book = xlrd.open_workbook(file)
    sh = book.sheet_by_index(0)
    for row_number in range(sh.nrows):
        row = sh.row_values(row_number)
        if row[1]:
            if row[0] != 'Итого:' and isinstance(row[1], float):
                articles.append(row[0])
                expenses.append(row[1])
    print_result(articles, expenses)


def print_result(articles, expenses):
    index_min = get_extreme_key(expenses, min)
    index_max = get_extreme_key(expenses, max)
    print('Минимальный расход:')
    print('Статья:', articles[index_min])
    print('Сумма:', expenses[index_min], 'руб.')
    print('----------------------')
    print('Максимальный расход:')
    print('Статья:', articles[index_max])
    print('Сумма:', expenses[index_max], 'руб.')


def get_extreme_key(array, compare):
    extreme_index = 0
    extreme = array[extreme_index]
    i = 1
    while i < len(array):
        if compare(array[i], extreme) == array[i]:
            extreme = array[i]
            extreme_index = i
        i += 1
    return extreme_index


if __name__ == '__main__':
    # parsing(FILE)
    do(FILE)

