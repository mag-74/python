# ЗАДАНИЕ №3 ИЗ ДОМАШКИ ВТОРОГО СЕМИНАРА

# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод.
print("\033[H\033[J")

                                                                    # БЫЛО
# import random
# n = int(random.randint(5,10))
# list = []
# for i in range(n):
#     list.append(random.randint(0,100))
# print(f'Исходный список: {list}')
# for i in range(len(list)):
#     j = random.randint(0, (len(list)-1))
#     list[i], list[j] = list[j], list[i]
# print(f'Список после перемешивания: {list}')
                                                                    # СТАЛО (ФИГНЯ УЛУЧШЕНИЙ, НО БЫЛ ПОВОД ВЕРНУТЬСЯ К НЕДОДЕЛАННОМУ ДЗ)
import random                                                                    
list = [random.randint(0,100) for _ in range(int(random.randint(5,10)))]                            # List Comprehension ++
print(f'Исходный список: {list}')
for i in range(len(list)):
    j = random.randint(0, (len(list)-1))
    list[i], list[j] = list[j], list[i]
print(f'Список после перемешивания: {list}')