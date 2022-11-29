# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.
print("\033[H\033[J")

import random
n = int(random.randint(5,10))
list = []
sum = 0
for i in range(n):
    list.append((1+1*i)**i)
    sum += (1+1*i)**i

print(f'Создан массив из {n} чисел:')
print(list)
print(f'Сумма всех его чисел равна: {sum}')
