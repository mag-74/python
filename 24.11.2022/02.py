# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
print("\033[H\033[J")
number = int(input('Введите число: '))
if (number%10 == 0 or number%15 == 0) and number%30 != 0:
    print('Условие выполнено')
else:
    print('Условие не выполнено')