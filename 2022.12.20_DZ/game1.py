import random
from bot_config import dp, bot
from aiogram import types

last_turn = 'comp'
bank = 150

async def start(message: types.Message):
    global bank, last_turn
    await bot.send_message(message.from_user.id, text = f'game1 слющает тибя аниматильна')
    while bank != 0:
        if last_turn == 'comp':
            user_move()
            bot.send_message(message.from_user.id, text = f'Вы забрали {user_move} шт., всего осталось {bank} шт.')
        else:
            comp_move()
            bot.send_message(message.from_user.id, text = f'Компьютер забирает {comp_move} шт., всего осталось {bank} шт.')
    if bank == 0:
        if last_turn == 'user':
            bot.send_message(message.from_user.id, text = f'Игра окончена. Вы победили!')
        else:
            bot.send_message(message.from_user.id, text = f'Игра окончена. Вы проиграли!') 

def input_user_move(message: types.Message):
    n = int(bot.send_message(message.from_user.id, text = f'Ваш ход! Введите число конфет от 1 до 28 штук, которые вы хотите сейчас забрать: '))
    if n < 1 or n > 28 or n > bank:
        bot.send_message(message.from_user.id, text = f'Вы ввели неверное число! Попробуйте снова!')
        n = input_user_move()
        return n
    else:
        return n

def user_move():
    global bank, last_turn
    user_move = input_user_move()
    bank = bank - user_move
    last_turn = 'user'

def comp_move():
    global bank, last_turn
    if bank < 29:
        comp_move = bank
    else:
        comp_move = bank%29
    bank = bank - comp_move
    last_turn = 'comp'