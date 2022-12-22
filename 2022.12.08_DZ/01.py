# ЗАДАНИЕ №2 ИЗ ДОМАШКИ ТРЕТЬЕГО СЕМИНАРА

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]
print("\033[H\033[J")
                                                                    # БЫЛО
# import random
# n = int(random.randint(3,10)) # Формируем массив случайного размера со случайными числами
# list = []
# for i in range(n):
#     list.append(int(random.randint(1,9)))
# print(f'Список из {n} чисел: {list}')
# rez = []
# for j in range(int(len(list)/2)): # Сначала считаем пары ...
#     rez.append(list[j]*list[int(len(list)-j-1)])
# if int(len(list))%2 != 0: # ... потом дорисовываем серединку, если число элементов в списке нечетное
#     rez.append(list[int((len(list)-1)/2)]**2)
# print(rez)
                                                                    # СТАЛО
import random
list = [random.randint(1,99) for _ in range(int(random.randint(3,9)))]                                     # List Comprehension ++
print(f'Список из {len(list)} чисел: {list}')
rez = []
for j in range(int(len(list)/2)):
    rez.append(list[j]*list[int(len(list)-j-1)])
if int(len(list))%2 != 0:
    rez.append(list[int((len(list)-1)/2)]**2)
print(rez)