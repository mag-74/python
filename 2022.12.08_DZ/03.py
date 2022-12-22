# ЗАДАНИЕ №1 ИЗ ДОМАШКИ ТРЕТЬЕГО СЕМИНАРА

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
print("\033[H\033[J")

                                                                    # БЫЛО
# import random
# n = int(random.randint(5,10))
# list = []
# for i in range(n):
#     list.append(random.randint(0,10))
# print(list)
# spisok = []
# sum = 0
# for i in range(1,len(list),2):
#     spisok.append(list[i])
#     sum = sum + list[i]
# print(f'Список чисел на нечетных позициях {spisok}, их сумма равна {sum}')

                                                                    # СТАЛО
import random
list = [random.randint(0,10) for _ in range(int(random.randint(5,10)))]              # List Comprehension ++
print(f'Дан исходный список: {list}')
sum = 0
spisok = [list[i] for i in range(1,len(list),2)]                                     # List Comprehension ++
for i in spisok:
    sum += i
print(f'Список чисел на нечетных позициях {spisok}, их сумма равна {sum}')