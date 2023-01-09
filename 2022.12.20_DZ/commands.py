from bot_config import dp, bot
from aiogram import types
import random

bank = 150

@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'Привет, {message.from_user.first_name}! Выбери команду: /game1')

@dp.message_handler(commands=['game1'])
async def start_game1(message: types.Message):
    await message.reply(f'{message.from_user.first_name}, ок! Сыграем в игру в конфетки! Правила такие: У нас есть 150 конфет! Каждый игрок за один ход может забрать от одной до 28 штук. Выиграет тот, кто сделает последний ход.')
    await bot.send_message(message.from_user.id, f'Ваш ход! Введите число конфет от 1 до 28 штук, которые вы хотите сейчас забрать: ')

@dp.message_handler()
async def play_game1(message: types.Message):
    global bank, last_turn
    if message.text.isdigit() and int(message.text) > 0 and int(message.text) < 29:
        while bank != 0:
            bank = bank - int(message.text)
            if bank == 0:
                await bot.send_message(message.from_user.id, text = f'Вы забрали последние конфеты и победили! Поздравляем!')
                break
            if bank < 29:
                comp_move = bank
            else: 
                comp_move = bank%29
            if comp_move == 0:
                comp_move = random.randint(1,28)
            bank = bank - comp_move
            await bot.send_message(message.from_user.id, text = f'Вы забрали {int(message.text)} шт., а бот - {comp_move}, всего осталось {bank} конфет.')
            if bank == 0:
                await bot.send_message(message.from_user.id, text = f'Бот забрал конфеты последним. Игра окончена и Вы проиграли!')
                break
            await bot.send_message(message.from_user.id, f'Ваш ход! Сколько конфет забираете Вы?')
            break
    else:
        await bot.send_message(message.from_user.id, f'Что-то не то ввели, давайте еще разок!')