# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k. Пример: если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
print("\033[H\033[J")
import random

k = int(random.randint(2,10))
koef = {}
for i in range(k+1):
    koef[i] = random.randint(0,100)
print(koef)

eq = ''
for i in range(k, -1, -1):
    if koef[i] != 0:
        if koef[i] == 1:
            if i == 1:
                eq += f'x + '
            elif i == 0:
                eq += f'1 '
            else:
                eq += f'x**{i} + '
        else:
            if i == 1:
                eq += f'{koef[i]}*x + '
            elif i == 0:
                eq += f'{koef[i]} '
            else:
                eq += f'{koef[i]}*x**{i} + '
eq += f'= 0'
eq = eq.replace('+ =','=')

print(f'У нас есть следующее выражение: {eq}')

with open('eq.txt', 'w', encoding='UTF-8') as data:
    data.write(eq)
data.close()
