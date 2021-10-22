FIND_DIRECTORY = 'Test'
import os
import re
import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def walk(directory):
    frequency = {}
    for root, dirs, files in os.walk(directory):  # рекурсивная функция
        for name in files:
            file = os.path.join(root, name)
            f = open(file, 'r', encoding='utf-8')
            new_frequency = analysis(f.read())
            f.close()
            for word in new_frequency:
                count = frequency.get(word, 0)
                frequency[word] = count + new_frequency.get(word)
            print_result(frequency)


def analysis(content):
    frequency = {}
    matches = re.findall(r'\b[а-я]+\b', content, re.IGNORECASE)
    for word in matches:
        word = word.lower()
        word = (morph.parse(word)[0].normal_form)
        count = frequency.get(word, 0)
        frequency[word] = count + 1
    return frequency


def print_result(frequency):
    frequency = sort(frequency)
    for word in frequency:
        print(word, frequency[word])


def sort(dictionary):
    sorted_dict = {}
    sorted_keys = sorted(dictionary, key=dictionary.get, reverse=True)
    for key in sorted_keys:
        sorted_dict[key] = dictionary[key]
    return sorted_dict


if __name__ == "__main__":
    walk(FIND_DIRECTORY)
