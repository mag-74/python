# Дан список чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность чисел в списке.
# Порядок элементов менять нельзя.
print("\033[H\033[J")

import random
list = [random.randint(0,10) for _ in range(10)]
print(f'Исходный список: {list}')

res = []

for i in range(len(list)-1):
    res.append(list[i])
    if list[i+1] > list[i]:
        for j in range(len(list)-1-i):
            if list[i+1+j] > list[i+j]:
                res.append(list[i])
        

# res.insert(0, list[i])
# res.append(i)
print(res)