# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Примеры: 6782 -> 23   0,56 -> 11
print("\033[H\033[J")

z = float(input('Введите число: '))

def sum_z(z):
    sum = 0
    for i in str(z):
        if i != ".":
            sum += int(i)
    return sum

print(f"Сумма цифр числа равна {sum_z(z)}")