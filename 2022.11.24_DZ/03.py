# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод.
print("\033[H\033[J")
import random
n = int(random.randint(5,10))
list = []
for i in range(n):
    list.append(random.randint(0,100))
print(f'Исходный список: {list}')
                                                # СВОЯ НЕРАБОЧАЯ ХРЕНЬ:
# list_new = [0]*len(list)
# k = 0
# if k < len(list): # Не хватает мозгов заставить программу возвращаться к генерации случайного места
#     for i in range(len(list)):
#         j = int(random.randint(0,len(list_new)-1))
#         if list_new[j] == 0:
#             list_new[j] = list[i]
#             k += 1
#         else:           
#             j = int(random.randint(0,len(list_new)-1))
                                                # ДОРАБОТАНО ПОСЛЕ ПЯТОГО СЕМИНАРА:
for i in range(len(list)):
    j = random.randint(0, (len(list)-1))
    list[i], list[j] = list[j], list[i]
print(f'Список после перемешивания: {list}')