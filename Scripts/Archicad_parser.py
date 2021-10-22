
calculation = 9430 + 220 + 3100 + 1426 + 2400 + 144 + 3705 + 1500 + 6235 + 3975 + 3275 + 215 + 4045 + 6978 + 2891 + 224 + 4034 + 2902 + 7214 + 4008 + 1505 + 310 + 3915


def Parsing_txt_file_from_Archicad(path, number_of_plains: int = 1, units_mm_to_meter: bool = True):
    path = open(path, "r", encoding='utf-8')
    content = (path.readlines())
    array = []
    nice_string = "0"
    summ = 1
    area_calc=0
    units =""


    for line in content:
        if len(line) > 1 and line[0:5] != "Линия" and line[0:5]!= "Штрих":
            if (line[0:5]) == "Длина":
                new_line = (line[7:])
                new_line_without_spaces = new_line.replace(u'\xa0', "")
                good_new_line = new_line_without_spaces.replace("мм", "")
                array.append(good_new_line.strip())
                summ = 0
                for n in array:
                    summ += int(n)
                    nice_string.join(n)
                units =" метров"
            else:
                if line[0:20]=="Площадь, отверстия р":
                    float_area = line[37:41]
                    new_f_a =float_area.replace(",",".")
                    array.append(str(new_f_a))
                    area_calc+=float(new_f_a)
                summ = round(area_calc,1)
                units ="м.кв."
    print("")
    print("")
    print("+".join(array))
    if units_mm_to_meter:
        summ = summ / 1000

    return summ * number_of_plains, units


if __name__ == "__main__":
    result = Parsing_txt_file_from_Archicad(path=r'../area.txt', number_of_plains=1, units_mm_to_meter=False)
    print(f'{result[0]}{result[1]}')


# todo Создать расчетчик строительного периметра (функция) Периметр в плоскости:
# Берем периметр в одной проекции и умножаем на кол-во плоскостей
