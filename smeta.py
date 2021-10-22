from Scripts.Archicad_parser import Parsing_txt_file_from_Archicad
"""

Погонаж коробов считается в плоскостях. Вертикальная плоскость 5 и горизонтальная 5.
Такой же учёт идёт в малярных и плиточных работах погонный изделий.
По той же схеме расчитывается и материал. То есть расход смесей, клея и плитки.
На горизонт и вертикальную плоскость. Суммируются погонные метры каждой плоскости изделия

Если ширина плоскости менее 600 мм  то считается погонаж и считается каждая плоскость


"""

# Высота чернового потолка 1й этаж
THE_HEIGHT_OF_THE_DRAFT_CEILING = 3.049
# Бетонные стены в сан.узлах:
CONCRETE_WALLS_WCS_2F = (2471 + 2887 + 1894 + 2902 + 2751) * THE_HEIGHT_OF_THE_DRAFT_CEILING / 1000
CONCRETE_WALLS_WCS_1F = (2399 + 3105 + 2909 + 2926 + 2264 + 1703) * THE_HEIGHT_OF_THE_DRAFT_CEILING / 1000
cwa = CONCRETE_WALLS_WCS_1F + CONCRETE_WALLS_WCS_2F
# Общая длина новых стен первый и второй этажи:
LENGTH_OF_NEW_WALLS = 7513 + 8254 + 2764 + 2788 + 3180 + 2960 + 1475 + 2000 + 2689 + 720 + 385 + 1426 + 2770 + 2020 + \
                      1440 + 2400 + 1440 + 1900 + 2632 + 300 + 800 + 200 + 2915 + 2502 + 204 + 800 + 204 + 312 + 205 + 1000 \
                      + 205 + 1469 + 800 + 2316 + 800 + 520 + 4093 + 4000 + 2963 + 2500 + 604 + 600 + 195 + 2105 + 200 \
                      + 745 + 790 + 270 + 1130
# Площадь дверных проемов два этажа:
DOORS1 = (1200 + (900 * 7) + 1200) * 2700  # Площадь дверных проемов 1го этажа (9)
DOORS2 = ((900 * 8) + 800) * 2700  # Площадь дверных проемов 2го этажа (9)
DOORS = (DOORS1 + DOORS2) / 1000000
# Длина плинтуса два этажа из ведомости:
MY_PLINTUS = 5.2 + 8 + 8.9 + 9.4 + 2.3 + 1.3 + 6.3 + 9.8 + 15.3 + 7 + 10 + 12.6 + 15.2 + 8.3
# Длина плинтуса два этажа из чертежей (подсчитали чертёжницы):
PLINTUS_VEDOMOST = 71.8 + 42.7

# Подсчет скрытого плинтуса
PLINTUS_2_FLOOR = 296 + 3600 + 325 + 118 + 376 + 270 + 2700 + 564 + 2915 + 630 + 100 + 672 + 204 + 312 + 1469 + 520 + 20 \
                  + 740 + 4343 + 379 + 377 + 1505 + 125 + 383 + 370 + 930 + 900 + 70 + 848 + 2803 + 160 + 120 + 1860 \
                  + 1644 + 600 + 200 + 1003 + 2770 + 270 + 409 + 255 + 371 + 1475 + 278
PLINTUS_1_FLOOR = 72784
# Подсчет стены из бетона без плинтуса 1й этаж:

WALL_WITHOUT_PLINTUS_CONCRETE_1F = 4768 + 7191 + 2909 + 1683 + 5384 + 930

# Бетонная стена с плинтусом 1й этаж:
CONCRETE_PLINTUS_WALL_1F = 1512 + 1093 + 2851 + 4585 + 3968 + 1503 + 327 + 1500 + 3939 + 2889 + 236 + 3026 + 1567 + 3736 + 3338 + 3925 + 1507 + 229 + 1590
CONCRETE_PLINTUS_WALL_2F = 3275 + 276 + 2700 + 564 + 376 + 270 + 4343 + 359 + 358 + 1525 + 125 + 363 + 350
all_beton_wall_with_plintus = (CONCRETE_PLINTUS_WALL_1F + CONCRETE_PLINTUS_WALL_2F)/1000 # Стены, где плинтус по бетону
# Площадь стен из сметы Сергея:
SERGEYS_WALLS = 116.5 + 169.36
# Площадь стен из сметы Андрея:
ANDREYS_WALLS = 213.43 + 13.91

# Кол-во инсталляций для унитаза:
INSTALLATIONS = 3
# Периметр линии потолка (теневой профиль) второго этажа:
CEILING_PERIMETER_2ST_FLOOR = 16820 + 29222 + 25220 + 10826 + 16446 + 16592 + 10882 + 17426 + 10190 + 22166
# Площадь потолка 2 этажа:
CEILING_AREA_2ST_FLOOR = 146.62
# Периметр линии потолка (теневой профиль) 1 этажа:
CEILING_PERIMETER_1ST_FLOOR = 16982 + 16808 + 11009 + 69795 + 10789 + 9185 + 9046 + 10416
# Площадь потолка 1 этажа:
CEILING_AREA_1ST_FLOOR = (127 + 33.3)

led_line_2_floor = Parsing_txt_file_from_Archicad(r'led_line_2floor.txt',1,True)  # Потолочная LED лента 2 этаж
led_line_1_floor = Parsing_txt_file_from_Archicad(r'led_line_1_floor.txt',1,True)  # Потолочная LED лента 1 этаж

WC_AREA = 7.3 + 5.03 + 4.25 + 6.68 + 1.74 + 7.65
ceiling = CEILING_AREA_1ST_FLOOR + CEILING_AREA_2ST_FLOOR  # площадь всех потолков
ceiling_perimeter = CEILING_PERIMETER_1ST_FLOOR + CEILING_PERIMETER_2ST_FLOOR  # периметр всех потолков
# Кол-во дверей:
HOW_MUCH_DOORS = 20
# Периметр бетонных стен на 1 этаже:
CONCRETE_WALLS_PERIMETER_1_FLOOR = 82608
# Периметр бетонных стен на 2 этаже:
CONCRETE_WALLS_PERIMETER_2_FLOOR = 1855 + 144 + 3705 + 1500 + 6235 + 3975 + 3275 + 3255 + 4025 + 6958 + 2815 + 2555 + 9430 + 3915 + 1505 + 105 + 4008 + 4363 + 1730 + 2902 + 1172 + 4019 + 2891 + 104
# Периметр стен ГКЛ на 1 этаже для шпатлевания (2 стороны):
KNAUF_WALLS_PERIMETER_1_FLOOR = 4018 + 3085 + 2860 + 2664 + 2285 + 2764 + 2960 + 2788 + 100 + 529 + 2000 + 530 + 2689 + \
                                980 + 2059 + 1077 + 600 + 2909 + 1021 + 1003 + 605 + 1264 + 439 + 1255 + 1260 + 75 + 140 + \
                                3621 + 2264 + 2750 + 300 + 250 + 1963 + 900 + 385 + 720 + 620 + 1200 + 1983 + 5667

# Периметр стен ГКЛ на 2 этаже для шпатлевания (2 стороны):
KNAUF_WALLS_PERIMETER_2_FLOOR = 32882 + 3052

# Периметр стен с плиткой на 1 этаже:
PERIMETER_OF_THE_WALLS_UNDER_THE_TILE_1ST_FLOOR = 1988 + 1400 + 2909 + 1021 + 900 + 605 + 109 + 2417 + 439 + 1264 + 1703 \
                                                  + 2750 + 2264 + 2500 + 1963 + 250 + 300 - 430 - 1020 - 2045 - 364 - 419 - 585 - 1021 - 2819
# Периметр стен с плиткой на 2 этаже:
PERIMETER_OF_THE_WALLS_UNDER_THE_TILE_2ST_FLOOR = 1260 + 455 + 50 + 800 + 1281 + 1000 + 1298 + 270 + 790 + 745 + 15 + 1343 + \
                                                  760 + 5 + 1605 + 600 + 1304 + 205 + 115 + 770 + 0 + 200 + 2400 + 2105 + \
                                                  195 + 90 + 105 + 900 + 300 + 1804 + 1095 + 604 + 58

tiling_walls_area = (((
                              PERIMETER_OF_THE_WALLS_UNDER_THE_TILE_1ST_FLOOR + PERIMETER_OF_THE_WALLS_UNDER_THE_TILE_2ST_FLOOR) * 2.7) / 1000) - (
                            4 * 2.7 * 0.8)

# Внешние углы ГКЛ стен 1 этаж:
EXTERNAL_KNAUF_CORNERS_1ST_FLOOR = 16
# Внутренние углы ГКЛ стен 1 этаж:
INTERNAL_KNAUF_CORNERS_1ST_FLOOR = 37

# Внешние углы ГКЛ стен 2 этаж:
EXTERNAL_KNAUF_CORNERS_2ST_FLOOR = 10
# Внутренние углы ГКЛ стен 2 этаж:
INTERNAL_KNAUF_CORNERS_2ST_FLOOR = 31


# todo: посчитать откосы входной двери

SLOPES_OF_THE_ENTRANCE_DOORS_1F = ((
                                           0.240 * 2.100 * 2) + 0.25) + 0.1 * 2.7 * 2 * 3  # откосы входной и раздвижной двери 1й этаж

# Периметр внешних поверхностей не закрытых ГКЛ бетонных стен 1й этаж:
PERIMETER_OF_EXTERNAL_SURFACES_CONCRETE_1ST_FLOOR = 915 + 1512 + 1098 + 606 + 145 + 1990 + 2065 + 2004 + 2664 + 199 + 3968 \
                                                    + 1503 + 100 + 107 + 3979 + 4585 + 2526 + 2909 + 1703 + 2500 + 226 + \
                                                    3026 + 6971 + 4006 + 3258 + 220 + 3965 + 1507 + 189 + 1957

# Периметр внешних поверхностей не закрытых ГКЛ бетонных стен 2й этаж без вычета кирпичных участков:
PERIMETER_OF_EXTERNAL_SURFACES_CONCRETE_2ST_FLOOR = 3975 + 2720 + 3275 + 4618 + 98 + 2260 + 2835 + 2400 + 1804 + 1095 + \
                                                    1605 + 1630 + 1343 + 4363 + 4008 + 1505 + 105 + 3915 + 9430 + 2555 + \
                                                    1855 + 144 + 3705 + 1500 + 3415 + 4045

# Кирпичные участки стен 2 этажа:
PERIMETER_OF_BRICK_WALLS = 1500 + 4735
# Периметр проема заделанного блоками на 2 этаже:
PERIMETER_OF_BLOCK_WALL_2ST_FLOOR = 1148  # Площадь блоков в дверном проёме 2этаж
AREA_OF_BLOCK_WALL_2ST_FLOOR = 1148 * 2100

# Площадь окон 1й этаж (5):
WINDOWS_AREA_1ST_FLOOR = (3652 * 2895) + (3305 * 1906) + (3306 * 1902) + (3301 * 1900) + (3301 * 1893)
# Площадь окон второй этаж (4):
WINDOWS_AREA_2ST_FLOOR = (3348 * 2740) + (3300 * 2740) + (3202 * 2719) + (3292 * 2738)

PAINTING = 468  # Площадь покраски стен
STUCCO_WALLS = 116  # Площадь декоративной штукатурки
FLOOR_WOODEN = 117 + 129.17  # Площадь деревянного пола
FLOOR_TILING = 63 + 7.65 + 1.74 + 6.88  # Площадь плиточного пола

WINDOWS_PERIMETER_1_FLOOR = 2895 + 2895 + 3652 + (3305 + 1906 + 1906) * 4  # Периметр откосов окон 1й этаж
WINDOWS_PERIMETER_2_FLOOR = (3300 + 2740 + 2740) * 4  # Периметр откосов окон 2й этаж

WINDOWS_PERIMETER_1_FLOOR2 = 2895 + 2895 + 3652 + (
        3305 + 3305 + 1906 + 1906) * 4  # Периметр откосов окон 1й этаж с подоконником
WINDOWS_PERIMETER_2_FLOOR2 = (3300 + 3300 + 2740 + 2740) * 4  # Периметр откосов окон 2й этаж с подоконником
# Расчет площади бетонных стен под грунтовку:
concrete_walls_area = ((
                               CONCRETE_WALLS_PERIMETER_1_FLOOR / 1000 + CONCRETE_WALLS_PERIMETER_2_FLOOR / 1000 - PERIMETER_OF_BRICK_WALLS / 1000) * THE_HEIGHT_OF_THE_DRAFT_CEILING) - DOORS


PERIMETER_OF_FALSE_WALLS_1ST_FLOOR = (1400+1863+309+300)/1000
PERIMETER_OF_FALSE_WALLS_2ST_FLOOR = (2500+420+1030+1383+1426)/1000
ALL_FALS_WALLS_AREA = (PERIMETER_OF_FALSE_WALLS_1ST_FLOOR+PERIMETER_OF_FALSE_WALLS_2ST_FLOOR)*THE_HEIGHT_OF_THE_DRAFT_CEILING
ALL_FALS_WALLS_PERIMETR = (PERIMETER_OF_FALSE_WALLS_1ST_FLOOR+PERIMETER_OF_FALSE_WALLS_2ST_FLOOR) # Периметр фальш стен


if __name__ == "__main__":
    print(f"Площадь новых стен за вычетом дверей: {((LENGTH_OF_NEW_WALLS * 3047 - DOORS) / 1000000)}\n")
    print(f"Площадь новых стен без вычета дверей: {((LENGTH_OF_NEW_WALLS * 3047) / 1000000)}\n")
    print(f"Площадь стен у Сергея: {SERGEYS_WALLS}\n")
    print(f"Площадь стен у Андрея: {ANDREYS_WALLS}\n")
    print(f'Плинтус из ведомости: {MY_PLINTUS}\n')
    print(f'Плинтус из чертежей: {PLINTUS_VEDOMOST}\n')
    print(f'Периметр откосов окон 1й этаж: {WINDOWS_PERIMETER_1_FLOOR / 1000}\n')
    print(f'Периметр откосов окон 2й этаж: {WINDOWS_PERIMETER_2_FLOOR / 1000}\n')
    print(f'Периметр откосов окон этаж: {(WINDOWS_PERIMETER_2_FLOOR + WINDOWS_PERIMETER_1_FLOOR) / 1000}\n')
    print(
        f'Периметр откосов окон этаж с подоконными откосами: {(WINDOWS_PERIMETER_2_FLOOR2 + WINDOWS_PERIMETER_1_FLOOR2) / 1000}\n')
    print(f'Пол плитка {FLOOR_TILING}\n')
    print(f'Пол с инженерной доской: {FLOOR_WOODEN}\n')
    print(f'Весь пол: {FLOOR_TILING + FLOOR_WOODEN}\n')

    # Периметр перегородок ГКЛ*2700/1000000 = Площадь звукоизоляции внутренних перегородок
    a = ((LENGTH_OF_NEW_WALLS * 2700) - DOORS) / 1000000
    print(f'Площадь звукоизоляции перегородок из ГКЛ: {a}\n')
    print(f'Площадь плиточного пола: {FLOOR_TILING}, Площадь мокрых зон в с.у: {WC_AREA}\n')
    print(f'Откосы дверей 1го этажа: {SLOPES_OF_THE_ENTRANCE_DOORS_1F}\n')
    print(f'Площадь потолков: {ceiling}\n')
    print(f'Периметр потолков: {ceiling_perimeter / 1000}\n')

    # Стены из плитки:
    print(f'Стены из плитки: {tiling_walls_area}\n')
    print(f'Площадь бетонных стен: {concrete_walls_area}\n')
    print(f'Площадь бетонных стен в санузлах: {cwa}\n')
    print(f'Плинтус 1й этаж: {PLINTUS_1_FLOOR / 1000}\n')
    print(f'Плинтус на бетонной стене 1й этаж: {CONCRETE_PLINTUS_WALL_1F / 1000}\n')
    print(f'Плинтус на бетонной стене 2й этаж: {CONCRETE_PLINTUS_WALL_2F / 1000}\n')
    print(f'Плинтус на бетонной стене: {(CONCRETE_PLINTUS_WALL_2F+CONCRETE_PLINTUS_WALL_1F) / 1000}\n')
    print(f'Плинтус 2й этаж: {PLINTUS_2_FLOOR / 1000}\n')
    print(f'Плинтус всего: {(PLINTUS_2_FLOOR + PLINTUS_1_FLOOR) / 1000}\nПлинтус по бетону: {all_beton_wall_with_plintus}\n'
          f'Плинтус по ГКЛ: {((PLINTUS_2_FLOOR + PLINTUS_1_FLOOR) / 1000)-all_beton_wall_with_plintus}\n')
    print(f'Площадь фальш стен: {ALL_FALS_WALLS_AREA}, Периметр: {ALL_FALS_WALLS_PERIMETR}\n')
    print (f'Led лента потолок второй этаж: {led_line_2_floor[0]} {led_line_2_floor[1]}\n')
    print(f'Led лента потолок первый этаж: {led_line_1_floor[0]} {led_line_1_floor[1]}\n')
    print(f'Led лента потолок 1,2 этажи: {led_line_1_floor[0]+led_line_2_floor[0]} {led_line_1_floor[1]}\n')
