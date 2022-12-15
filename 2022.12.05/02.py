# Дан список чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность чисел в списке.
# Порядок элементов менять нельзя.
print("\033[H\033[J")

import random
my_list = [random.randint(0,10) for _ in range(10)]
print(f'Исходный список: {my_list}')
new_list = []
for i in range(len(my_list)):
    result = []
    max = my_list[i]
    result.append(my_list[i])
    for j in range(i+1, len(my_list)):
        if my_list[j] > max:
            result.append(my_list[j])
            max = my_list[j]
    if len(result) > 1:
        new_list.append(result)
print(f'Cписок всех групп чисел по возрастанию: {new_list}')

max = 0
for k in range(len(new_list)):
    if len(new_list[k]) > len(new_list[max]):
        max = k
print(f'Самая длинная группа чисел с возрастанием: {new_list[max]}')
