# Создайте программу для игры в "Крестики-нолики".
print("\033[H\033[J")

import random

cell = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
last_turn = 'None'
win_set = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)) # Сам не додумался, взял со стрима
comp_move: int

def print_set():
    print(f' {cell[0]} | {cell[1]} | {cell[2]} ')
    print('-----------')
    print(f' {cell[3]} | {cell[4]} | {cell[5]} ')
    print('-----------')
    print(f' {cell[6]} | {cell[7]} | {cell[8]} ')

def f_user_move():
    global last_turn, cell
    while last_turn == 'comp' or last_turn == 'None':
        user_move = int(input(f'В какую клетку вы ставите крестик? Введите число от 1 до 9: '))
        if cell[user_move-1].isdigit() and 10 > user_move > 0:
            cell[user_move-1] = 'X'
            last_turn = 'user'        
        else:
            print(f'Вы ввели некорректное число. Попробуйте снова!') 
    print("\033[H\033[J")
    print_set()

def f_comp_move():
    global last_turn, cell, comp_move
    if last_turn == 'None': # На случай первого хода
        cell[random.randint(1, 9)-1] = 'O'
        last_turn = 'comp'
        print("\033[H\033[J")
        print(f'Компьютер начинает игру и делает свой ход:') 
        print_set()        
    else:
        while last_turn == 'user':
            comp_move = random.randint(1, 9)
            if cell[comp_move-1].isdigit():
                cell[comp_move-1] = 'O'
                last_turn = 'comp'
        print("\033[H\033[J")
        print(f'Компьютер делает новый ход:') 
        print_set()

if int(random.randint(0,1)) == 0: # Решаем, кто делает первый ход!
    print(f'Вам выпал жребий первым сделать ход!')
    print_set()
    f_user_move()
else:
    f_comp_move()

def check_win() -> bool: # Сам не додумался, взял со стрима
    global cell, win_set
    for opt in win_set:
        if (cell[opt[0]] == cell[opt[1]] == cell[opt[2]]):
            return True
    return False

while check_win() == False:
    if last_turn == 'comp':
        f_user_move()
    else:
        f_comp_move()
else:
    if last_turn == 'user':
        print(f'Игра окончена. Вы победили!')
    else:
        print(f'Игра окончена. Вы проиграли!')
