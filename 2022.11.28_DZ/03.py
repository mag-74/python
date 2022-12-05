# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
print("\033[H\033[J")

import random
n = int(random.randint(6,20)) # Формируем массив случайного размера со случайными числами
list = []
for i in range(n):
    z = int(random.randint(0,5)) # При этом рандомно округляем
    temp = float(random.uniform(0,999))
    list.append(round(temp,z))
print(f'Список из {n} чисел: {list}')

list1 = []
for i in range(len(list)):
    if float.is_integer(list[i]) == False:
        list1.append(str(list[i]))
print(f'Список без целых чисел: {list1}')

# list2 = []
for item in list1:
    k = 0
    for char in item:
        k += 1
        if char == '.':
            print(f'Точка в {item} на позиции {k}')
            
#     list2.append(str(list1).split('.'))
# print(f'Список только дробных частей чисел: {list2}')