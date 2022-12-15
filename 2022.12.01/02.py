# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
print("\033[H\033[J")

string = input('Введите два числа через пробел: ')
print(string)
string = string.strip().split(' ')
for i in range(len(string)):
    string[i] = int(string[i])
print(string)

k = 1
while max(*string)*k%min(*string) != 0: # Первый вариант решения
    k += 1
print(max(*string)*k)

# for i in range(max(string), string[0]*string[0]+1): # Второй вариант решения
#     if i % string[0] == 0 and i % string[1] == 0:
#         print(i)
#         break