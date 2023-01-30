import random

total = 150
player_one_name = ''
player_two_name = ''
current_player = player_one_name
game_bot_mode = False


def set_max_total():
    global total
    while True:
        try:
            total = int(input('Введите общее количество конфет: '))
            break
        except ValueError:
            print('В цифрах введите, будьте добры')


def get_total():
    global total
    return total


def set_total(take: int):
    global total
    total -= take


def get_current_player_name():
    global current_player
    return current_player


def switch_player():
    global current_player
    global player_one_name
    global player_two_name
    if current_player == player_one_name:
        current_player = player_two_name
    else:
        current_player = player_one_name


def set_player_names():
    global player_one_name
    global player_two_name
    global game_bot_mode
    global current_player
    while player_one_name == '':
        player_one_name = input('Первый игрок представьтесь: ')
        current_player = player_one_name
    player_two_name = input('Второй игрок представьтесь '
                            '(Enter для игры против бота): ')
    if not player_two_name:
        player_two_name = 'Ботяо'
        game_bot_mode = True
    set_max_total()


def draw():
    return random.randint(0, 1)


def game_turn():
    global total
    global current_player
    switch_player()
    if current_player == player_two_name and game_bot_mode:
        take = bot_turn()
    else:
        take = player_turn()
    set_total(take)
    print(f'{current_player} взял {take} конфет. '
          f'На столе осталось {total}')


def bot_turn():
    global total
    take = 0
    if total <= 28:
        take = total
    else:
        take = total % 29
        if take == 0:
            take = random.randint(1, 28)
    return take


def player_turn():
    take = 0
    while True:
        try:
            take = int(input(f'{current_player}, '
                             f'cколько конфет хочешь взять? '))
            if 0 < take < 29:
                break
            elif take > 28:
                print(f'{current_player}, не жадничай, бери не больше 28')
            else:
                print(f'{current_player}, хоть че-нить надо взять! Не стесняйся...')
        except ValueError:
            print('Введи цифрами')
    return take