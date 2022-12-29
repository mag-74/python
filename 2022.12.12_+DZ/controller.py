from decimal import Decimal
import view, model, operations, logger

def input_first():
    number = view.input_number()
    model.set_first(number)

def input_second():
    while True:
        number = view.input_number()
        if model.get_operation() == '/' and number == 0:
            view.print_division_by_zero()
        else:
            model.set_second(number)
            break

def input_operation():
    oper = view.input_operation()
    model.set_operation(oper)

def solution():
    logger.save_data_base(f'Запущена процедура простого расчета')
    oper = model.get_operation()
    if oper == '+':
        model.addition()
    elif oper == '-':
        model.difference()
    elif oper == '*':
        model.multiplication()
    elif oper == '/':
        model.division()
    result_string = f'{model.get_first()} {model.get_operation()} {model.get_second()} = {model.get_result()}'
    view.print_to_console(result_string)
    model.set_first(model.get_result())

def start(): #                                                       ++ доработал
    logger.save_data_base(f'СЕССИЯ НАЧАТА')
    initial_input = view.initial_input()
    if initial_input.isdigit():
        logger.save_data_base(f'Введено число {initial_input}')
        print('Активирован режим обычного калькулятора')
        logger.save_data_base(f'Активирован режим обычного калькулятора')
        model.set_first(int(initial_input))
        while True:
            input_operation()
            if model.get_operation() == '=':
                logger.save_data_base(f'СЕССИЯ ЗАВЕРШЕНА')
                logger.save_data_base(f'\n')
                view.log_off()
                break
            input_second()
            solution()
    else:
        logger.save_data_base(f'Введено выражение {initial_input}')
        print('Вы ввели сложнейшее уравнение! Активирован режим суперкалькулятора!!!')
        logger.save_data_base(f'Активирован режим суперкалькулятора')
        first_input(initial_input)


def first_input(number): #                                                   ++ вкручено готовое и немного напильником
    while True:
        number = number.strip().replace(' ', '').replace('+', ' + ').replace('-', ' - '). \
            replace('*', ' * ').replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ').split()
        logger.save_data_base(f'Выражение очищено от лишних пробелов и непечатываемых символов')
        if number[0] == '-':
            number[0] = number[0] + number[1]
            number.pop(1)
        if len(number) < 2:
            number = float(number[0])
            number = str(number)
            number = Decimal(number)
            # simple_calculate(number)
        else:
            if validator_expression(number):
                string_expression(number)
            else:
                print('Введено некорректное выражение')
                logger.save_data_base(f'Пользователю дан ответ: введено некорректное выражение')
        result = model.get_result()
        view.print_result(result)
        retry = input('Посчитать еще одно выражение? (y/n)')
        if retry == 'y': #                                                   ++
            logger.save_data_base(f'Пользователь выбрал вариант продолжения работы')
            start()
        else:
            print('С вами приятно работать! Заходите еще!')
            logger.save_data_base(f'Пользователь выбрал вариант завершения работы')
            logger.save_data_base(f'СЕССИЯ ЗАВЕРШЕНА')
            logger.save_data_base(f'\n')
            break

# def simple_calculate(first_number: Decimal): #                                                   ++ вкручено готовое
#     logger.save_data_base(f'Запущена процедура расчета простой операции')
#     result = 0
#     model.set_memory(first_number)
#     while True:
#         oper = view.input_operation()
#         model.set_operation(oper)
#         if oper == '=':
#             break
#         number = view.input_number('Введите число: ')
#         model.set_number(number)
#         first = model.get_memory()
#         oper = model.get_operation()
#         second = model.get_number()
#         for operation in operations.operation:
#             if oper == operation:
#                 result = operations.operation.get(oper)(first, second)
#                 logger.save_data_base(f'Произведен расчет выражения: {first} {oper} {second}')
#         view.print_result(result)
#         model.set_memory(result)
#         model.set_result(result)

def string_expression(expression: list): #                                                   ++ вкручено готовое
    logger.save_data_base(f'Запущена процедура анализа выражения на наличие в нем скобок')
    result = 0
    if '(' in expression:
        result = string_calculate(check_parentheses(expression))
        logger.save_data_base(f'Получен результат: {result}')
    else:
        result = string_calculate(expression)
        logger.save_data_base(f'Получен результат: {result}')
    model.set_result(result)

def string_calculate(expression: list): #                                                   ++ вкручено готовое
    logger.save_data_base(f'Запущена процедура расчета строкового выражения')
    new_expression = []
    for item in expression:
        if isinstance(item, Decimal):
            new_expression.append(Decimal(item))
        else:
            new_expression.append(item)
    logger.save_data_base(f'Из выражения сформирован список: {new_expression}')
    while len(new_expression)>1:
        i = 0
        while (('*' in new_expression) or ('/' in new_expression)) and i < len(new_expression):
            if new_expression[i] in ['*', '/']:
                result = operations.operation.get(new_expression[i])(Decimal(new_expression[i-1]), Decimal(new_expression[i+1]))
                new_expression[i-1] = result
                new_expression.pop(i)
                new_expression.pop(i)
            i += 1
        while (('+' in new_expression) or ('-' in new_expression)) and i < len(new_expression):
            if new_expression[i] in ['+', '-']:
                result = operations.operation.get(new_expression[i])(Decimal(new_expression[i - 1]), Decimal(new_expression[i + 1]))
                new_expression[i - 1] = result
                new_expression.pop(i)
                new_expression.pop(i)
            i += 1
    logger.save_data_base(f'Процедура расчета строкового выражения вернула значение: {new_expression[0]}')
    return new_expression[0]

def check_parentheses(expression): #                                                   ++ вкручено готовое
    logger.save_data_base(f'Запущена процедура проверки корректности ввода скобок в выражении')
    while '(' in expression:
        open_index, close_index = 0, 0
        for i in range(len(expression)):
            if expression[i] == '(':
                open_index = i
            if expression[i] == ')':
                close_index = i
                break
        else:
            break
        first_expression = expression[0:open_index]
        part_expression = expression[open_index + 1:close_index]
        last_expression = expression[close_index + 1:]
        expression = first_expression + [string_calculate(part_expression)] + last_expression
    logger.save_data_base(f'Процедура проверки корректности ввода скобок в выражении вернула список: {expression}')
    return expression

def validator_expression(expression): #                                                   ++ вкручено готовое
    logger.save_data_base(f'Запущена процедура проверки корректности написания выражения')
    stack = []
    for char in expression:
        if char == '(':
            stack.insert(0, char)
        if char == ')':
            if len(stack) > 0:
                stack.pop(0)
            else:
                return False
    if len(stack) > 0:
        logger.save_data_base(f'Процедура проверки пройдена: False')
        return False
    else:
        logger.save_data_base(f'Процедура проверки пройдена: True')
        return True