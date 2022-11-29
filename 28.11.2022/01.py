# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
print("\033[H\033[J")

my_list = ['24t2t2t', 'vnbj173876439', '232fgdfbnn7643', 'fdbfjbndkjfnb1314424']
number = input('Введите символ, который ищем: ')
for item in my_list:
    for char in item:
        if char == number:
            print(f'Символ {number} присутствует в строке {item}')
            break
    else:
        print(f'Символ {number} не присутствует в строке {item}')