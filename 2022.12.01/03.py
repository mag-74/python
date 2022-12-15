# Найдите корни квадратного уравнения Ax² + Bx + C = 0 с помощью математических формул нахождения корней квадратного уравнения
print("\033[H\033[J")

equation = '12*x**2 + 7*x + 5 = 0'
equation = equation.replace(' ', '')
print(equation)
equation = equation[:-2].split('+')
print(equation)
new_equation = []
for item in equation:
    new_equation.append(item.split('*x')[0])
print(new_equation)

a, b, c = new_equation

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')