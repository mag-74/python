# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
print("\033[H\033[J")
string = input('Введите числа через пробел: ')
print(string)
string = string.split(' ')
# print(string)
for i in range(len(string)):
    string[i] = int(string[i])

print(f'Максимальное число {max(string)}, минимальное {min(string)}')