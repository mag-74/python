# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
print("\033[H\033[J")

import random
n = int(random.randint(5,30))
list = []
for i in range(n):
    list.append(random.randint(0,10))
print(list)

# Первое решение
# count = 0
# list2 = []
# for i in range(len(list)):
#     if list.count(list[i]) == 1:
#         list2.append(list[i])
# print(list2)

# Второе решение
# dict={}
# for i in list:
#     if i in dict.keys():
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)

# new_list=[]
# for j in dict.keys():
#     if dict[j]==1:
#         new_list.append(j)
# print(new_list)

# Третье решение
dict={}
for item in list:
    dict[item] = dict.get(item, 0) + 1
new_list=[]
for key, value in dict.items():
    if value == 1:
        new_list.append(key)
print(new_list)