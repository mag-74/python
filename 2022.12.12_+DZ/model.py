from decimal import Decimal

first_number = 0
second_number = 0
operation = ''
result = 0
#                                                   ++ вкручено готовое
memory = 0 
new_number = 0

def get_first():
    global first_number
    return first_number
def set_first(value):
    global first_number
    first_number = value


def get_second():
    global second_number
    return second_number
def set_second(value):
    global second_number
    second_number = value


def get_operation():
    global operation
    return operation
def set_operation(oper):
    global operation
    operation = oper


def get_result():
    global result
    return result
def set_result(value: Decimal): #                                                   ++ вкручено готовое
    global result
    result = value


def addition():
    global first_number, second_number, result
    result = first_number + second_number


def difference():
    global first_number, second_number, result
    result = first_number - second_number


def multiplication():
    global first_number, second_number, result
    result = first_number * second_number


def division():
    global first_number, second_number, result
    result = first_number / second_number
    if result == int(result):
        result = int(result)

def get_memory(): #                                                   ++ вкручено готовое
    global memory
    return memory
def set_memory(value: Decimal):
    global memory
    memory = value