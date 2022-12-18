# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
print("\033[H\033[J")
import random
#                                         # Генерация выражений и запись в файл
def gen_koef(k) -> dict:
    koef = {}
    for i in range(k, -1, -1):
        koef[i] = random.randint(0,100)
    return koef

def gen_eq(input_dict) -> str:
    k = len(input_dict)
    eq = ''
    for key, value in input_dict.items():
        if value != 0:
            if value == 1:
                if key == 1:
                    eq += f'x + '
                elif key == 0:
                    eq += f'1 '
                else:
                    eq += f'x**{key} + '
            else:
                if key == 1:
                    eq += f'{value}*x + '
                elif key == 0:
                    eq += f'{value} '
                else:
                    eq += f'{value}*x**{key} + '
    eq += f'= 0'
    eq = eq.replace('+ =','=')
    return eq

with open('eq1.txt', 'w', encoding='UTF-8') as data1:
    data1.write(gen_eq(gen_koef(int(random.randint(2,10)))))
with open('eq2.txt', 'w', encoding='UTF-8') as data2:
    data2.write(gen_eq(gen_koef(int(random.randint(2,10)))))

                                        # Чтение выражений из файла, обработка и запись в новый файл
eq1 = open('eq1.txt').read()
eq2 = open('eq2.txt').read()
print(f'Из файлов получены два выражения:')
print(f'1) {eq1}')
print(f'2) {eq2}')

def parsing_str(equation) -> dict:
    equation = equation.replace(' ', '')
    equation = equation[:-2].split('+')
    new_equation = []
    for item in equation:
        if item.isdigit():
            new_equation.append((item + ' 0').split())
        elif item == 'x':
            new_equation.append(('1' + item + '1').split('x'))
        elif item.endswith('x'):
            new_equation.append((item + '1').split('*x'))
        elif item.startswith('x'):
            new_equation.append(('1' + item).split('x**'))
        else:
            new_equation.append(item.split('*x**'))
    equation_dict = {}
    for item in new_equation:
        equation_dict[int(item[1])] = int(item[0])
    return equation_dict

eq1_dict = {}
eq2_dict = {}
eq1_dict = parsing_str(eq1)
eq2_dict = parsing_str(eq2)

def equation_sum(first: dict, second: dict) -> dict:
    base = first.copy()
    base.update(second)
    for key in base:
        if first.get(key) and second.get(key):
            base[key] = first.get(key) + second.get(key)
    return base

eq_sum_dict = equation_sum(eq1_dict, eq2_dict)
k = len(eq_sum_dict)
eq_sum = gen_eq(eq_sum_dict)
print(f'Сумма выражений получена и записана в новый файл:')
print(f'{eq_sum}')

with open('eq_sum.txt', 'w', encoding='UTF-8') as data_sum:
    data_sum.write(eq_sum)