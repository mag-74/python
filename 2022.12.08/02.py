# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 
# Пример: 2+2 => 4;   1+2*3 => 7;    1-2*3 => -5;
print("\033[H\033[J")

import random                   # Генерим выражение
n = random.randint(3,10)
z = random.randint(0,9)
operators = ['+', '-', '/', '*']
equation = f'{z}'
for i in range(n):
    seting = random.randint(0,3)
    z = random.randint(0,9)
    equation = f'{equation} {operators[seting]} {z}'
print(equation)

list = equation.split(' ')          # Парсим выражение
print(list)

for i in range(len(list)):          # Числа в числа
    if list[i].isdigit():
        list[i] = int(list[i])
print(list)

res = 0
i = 0
while ('*' in list or '/' in list) and i < len(list):
    if list[i] == '*':
        res = list[i-1] * list[i+1]
        list.pop(i)
        list.pop(i)
        list[i-1] = res
        print(list)
    elif list[i] == '/':
        res = list[i-1] / list[i+1]
        list.pop(i)
        list.pop(i)
        list[i-1] = res
        print(list)
    else:
        i += 1

while ('+' in list or '-' in list) and i < len(list):
    if list[i] == '+':
        res = list[i-1] + list[i+1]
        list.pop(i)
        list.pop(i)
        list[i-1] = res
        print(list)
    elif list[i] == '-':
        res = list[i-1] - list[i+1]
        list.pop(i)
        list.pop(i)
        list[i-1] = res
        print(list)
    else:
        i += 1

print(list)