# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4 -> 1
# x=-34; y=-30 -> 3
print("\033[H\033[J")
print('Введите целое число, координату Х: ')
x = int(input())
print('Введите целое число, координату Y: ')
y = int(input())
if x == 0:
    print(f'Точка лежит на оси Y с координатами ({x}:{y})')
elif y == 0:
    print(f'Точка лежит на оси X с координатами ({x}:{y})')
elif x > 0 and y > 0:
    print(f'Точка находится в I четверти с координатами ({x}:{y})')
elif x < 0 and y > 0:
    print(f'Точка находится в II четверти с координатами ({x}:{y})')
elif x < 0 and y < 0:
    print(f'Точка находится в III четверти с координатами ({x}:{y})')
elif x > 0 and y < 0:
    print(f'Точка находится в IV четверти с координатами ({x}:{y})')