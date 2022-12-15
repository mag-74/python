# Создайте программу для игры с конфетами человек против компьютера. Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота "интеллектом"
print("\033[H\033[J")

import random
bank = 150
last_turn = None
print(f'Привет юзер-лузер. Сыграем в игру! Правила такие: У нас есть {bank} конфет! Каждый игрок за один ход может забрать не более чем 28 конфет. Выиграет тот, кто сделает последний ход.')

def input_user_move():
    n = int(input(f'Ваш ход! Введите число конфет от 1 до 28 штук, которые вы хотите сейчас забрать: '))
    if n < 1 or n > 28 or n > bank:
        print(f'Вы ввели неверное число! Попробуйте снова!')
        n = input_user_move()
        return n
    else:
        return n

def user_move():
    global bank, last_turn
    user_move = input_user_move()
    bank = bank - user_move
    last_turn = 'user'
    print("\033[H\033[J")
    print(f'Вы забрали {user_move} шт., всего осталось {bank} шт.')

def comp_move():
    global bank, last_turn
    if bank == 150:
        print(f'Компьютер делает свой ход первым!')
        comp_move = bank%29
    elif bank < 29:
        comp_move = bank
    else:
        if bank%29 == 0: # Хлюздит, когда начинает проигрывать. И берет 0 штук!
            comp_move = random.randint(1,28)
        else:
            comp_move = bank%29
    bank = bank - comp_move
    last_turn = 'comp'
    print("\033[H\033[J")
    print(f'Компьтер забирает {comp_move} шт., всего осталось {bank} шт.')

if int(random.randint(0,1)) == 0: # Решаем, кто делает первый ход!
    print(f'Вам выпал жребий первым сделать ход!')
    user_move()
else:
    comp_move()

while bank != 0:
    if last_turn == 'comp':
        user_move()
    else:
        comp_move()

if bank == 0:
    if last_turn == 'user':
        print(f'Игра окончена. Вы победили!')
    else:
        print(f'Игра окончена. Вы проиграли!')

# Короче, кажется я наделил "бота интеллектом"! Я не могу выиграть его теперь его же оружием. Он все равно побеждает)))
# МОЯ ПОБЕДА - это полностью первый код, который написал сам, без инета и прочих подсказок!