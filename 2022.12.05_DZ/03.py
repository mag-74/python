# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: 'aaaaagggghhllll' > '5a4g2h4l' и наоборот
print("\033[H\033[J")

import random
symbols = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] # индекс 0-25
string = ''
string_conv = ''

def string_gen_type1():
    global string
    n = random.randint(5,9) # Генерим число букв в повторе
    for i in range(n):
        k = random.randint(0,25)
        symbol = symbols[k]
        for j in range(random.randint(1,6)):
            string = string + symbol
    string = string.lower()
    print(f'Исходная строка сгенерирована: {string}')

def string_gen_type2():
    global string
    n = random.randint(5,9) # Генерим число букв в повторе
    for i in range(n):
        k = random.randint(0,25)
        l = random.randint(1,9)
        symbol = symbols[k].lower()
        if symbol not in string:
            string = f'{string}{l}{symbol}'
    print(f'Исходная строка сгенерирована: {string}')

def convert_type_1to2():
    global string_conv, string
    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count = count + 1
            i += 1
        string_conv += str(count) + string[i]
        i = i + 1
    # temp = None                                           Не работает правильно
    # for item in string:
    #     if item != temp:
    #         string_conv = f'{string_conv}{string.count(item)}{item}'
    #         temp = item
    print(f'Результат конвертации: {string_conv}')

def convert_type_2to1():
    global string_conv, string
    count = ''
    for char in string:
        if char.isdigit():
            count += char
        else:
            string_conv += char * int(count)
            count = ''
    print(f'Результат конвертации: {string_conv}')

if int(random.randint(0,1)) == 0:
    string_gen_type1()
    convert_type_1to2()
else:
    string_gen_type2()
    convert_type_2to1()
