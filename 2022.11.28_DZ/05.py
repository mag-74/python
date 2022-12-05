# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
print("\033[H\033[J")

import random
n = int(random.randint(3,10))
list = []
a, b = 0, 1
for i in range (n):
    list.insert(0, a)
    a, b = b, a - b
list.append(1)
a = list[n-1]
b = list[n]
for i in range(n-2):
    list.append(list[n-1+i] + list[n+i])

print(n)
print(list)