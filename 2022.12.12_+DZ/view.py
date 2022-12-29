from decimal import Decimal
import logger

def input_number() -> int:
    while True:
        try:
            number = int(input('Введите целое число: '))
            logger.save_data_base(f'Введено число {number}')
            return number
        except:
            print('Ошибка!')
            logger.save_data_base(f'Ошибка ввода')

def input_operation():
    while True:
        operation = input('Введите операцию ("=" для завершения): ')
        if operation in ['+', '-', '*', '/', '=']:
            logger.save_data_base(f'Введен оператор {operation}')
            return operation
        else:
            print('Введите корректную операцию!')
            logger.save_data_base(f'Ошибка ввода')

def print_to_console(value_text):
    print(f'Ваше выражение: {value_text}')
    logger.save_data_base(f'Сформировано выражение для расчета {value_text}')

def log_off():
    print('Задача решена!')

def print_division_by_zero():
    print('На ноль делить нельзя!')
    logger.save_data_base(f'Введено ошибочное значение: деление на ноль')

def initial_input(): #                                                   ++ вкручено готовое
    initial_input = input('Введите число или строчное выражение: ')
    return initial_input

def print_result(value: Decimal): #                                                   ++ вкручено готовое
    if value == int(value):
        print(f'Результат: {int(value)}')
        logger.save_data_base(f'Пользователю дан результат расчета: {int(value)}')
    else:
        print(f'Результат: {round(value,4)}')
        logger.save_data_base(f'Пользователю дан результат расчета: {round(value,4)}')