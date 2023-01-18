from bot_config import dp, bot
from aiogram import types
import random, markups as nav
import emoji
active_game = 0
bank = 150

@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.last_name}!', reply_markup=nav.mainMenu)

@dp.message_handler()
async def start_game1(message: types.Message):
    global bank, active_game
    if message.text == 'Игры':
        await bot.send_message(message.from_user.id, f'Играть так играть!', reply_markup=nav.gameMenu)
    elif message.text == 'Назад':
        await bot.send_message(message.from_user.id, f'Ну вот и главное меню!', reply_markup=nav.mainMenu)
    elif message.text == 'Игра в конфеты':
        await message.reply(f'{message.from_user.last_name}, ок! Сыграем в игру в конфетки! Правила такие: У нас есть 150 конфет! Каждый игрок за один ход может забрать от одной до 28 штук. Выиграет тот, кто сделает последний ход.')
        await bot.send_message(message.from_user.id, f'Ваш ход! Введите число конфет от 1 до 28 штук, которые вы хотите сейчас забрать: ')
        active_game = 1
    elif message.text == 'Крестики-нолики':
        await message.reply(f'{message.from_user.last_name}, ок! Сыграем в крестики-нолики! Правила обычные: три в ряд, кто первый - тот победил!')
        # await bot.send_message(message.from_user.id, f'Ваш ход! Введите число конфет от 1 до 28 штук, которые вы хотите сейчас забрать: ')
        active_game = 2
    elif active_game == 1:     
        if message.text.isdigit() and int(message.text) > 0 and int(message.text) < 29:
            while bank != 0:
                bank = bank - int(message.text)
                if bank == 0:
                    await bot.send_message(message.from_user.id, text = f'Вы забрали последние конфеты и победили! Поздравляем!')
                    await bot.send_message(message.from_user.id, f'Поиграй со мной еще!', reply_markup=nav.gameMenu)
                    break
                if bank < 29:
                    comp_move = bank
                else: 
                    comp_move = bank%29
                if comp_move == 0:
                    comp_move = int(random.randint(1,28))
                bank = bank - comp_move
                await bot.send_message(message.from_user.id, text = f'Вы забрали {int(message.text)} шт., а бот - {comp_move}')
                bank_candy = [emoji.emojize(':candy:')] * bank
                await bot.send_message(message.from_user.id, f'Всего осталось {bank} конфет: {" ".join(str(x) for x in bank_candy)}')
                if bank == 0:
                    await bot.send_message(message.from_user.id, text = f'Бот забрал конфеты последним. Игра окончена и Вы проиграли!')
                    await bot.send_message(message.from_user.id, f'Поиграй со мной еще!', reply_markup=nav.gameMenu)
                    break
                await bot.send_message(message.from_user.id, f'Ваш ход! Сколько конфет забираете Вы?')
                break
        else:
            await bot.send_message(message.from_user.id, f'Что-то не то ввели, давайте еще разок!')
    # if active_game == 2: 
    #     pass