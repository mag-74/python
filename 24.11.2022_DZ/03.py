# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод.
print("\033[H\033[J")

import random
n = int(random.randint(5,10))
list = []
for i in range(n):
    list.append(random.randint(0,100))

list_new = [None]*len(list)
busy_places = []
flag = 0

for i in range(len(list)):
    j = int(random.randint(0,len(list)))
    if list_new[j] == None:
        list_new[j] = list[i]
        i = i + 1
    else:
        i = i



print(n)
print(list)
print(list_new)
print(busy_places)