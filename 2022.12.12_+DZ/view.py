from decimal import Decimal
def input_number() -> int:
    while True:
        try:
            number = int(input('Введите целое число: '))
            return number
        except:
            print('Ошибка!')

def input_operation():
    while True:
        operation = input('Введите операцию ("=" для завершения): ')
        if operation in ['+', '-', '*', '/', '=']:
            return operation
        else:
            print('Введите корректную операцию!')

def print_to_console(value_text):
    print(value_text)

def log_off():
    print('Задача решена!')

def print_division_by_zero():
    print('На ноль делить нельзя!')

def initial_input(): #                                                   ++ вкручено готовое
    initial_input = input('Введите число или строчное выражение: ')
    return initial_input

def print_result(value: Decimal): #                                                   ++ вкручено готовое
    if value == int(value):
        print(f'Результат: {int(value)}')
    else:
        print(f'Результат: {round(value,4)}')