# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:    
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90
print("\033[H\033[J")
print('Введите числа')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))
e = int(input('e = '))
numbers = [a, b, c, d, e]
print (numbers)

max = numbers[0]
n_max = 0
for i in range(5):
    if numbers[i] > max:
        max = numbers[i]
        n_max = i
        i = i + 1
    else:
        i = i + 1
print (f'Максимальное число в массиве {max}, элемент в массиве номер: {n_max+1}')