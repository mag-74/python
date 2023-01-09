from bot_config import dp, bot
from aiogram import types

total = 150

@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                      f', ты написал мне "{message.text}"')
    await bot.send_message(386778464, text=f'А {message.from_user.first_name}'
                                         f', мне написал "{message.text}"')

@dp.message_handler()
async def anything(message: types.Message):
    global total
    if message.text.isdigit():
        total -= int(message.text)
        if 0 < int(message.text) < 29:
            await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                         f'взял со стола {message.text} конфет.'
                                                         f'На столе осталось {total}.')
        else:
            await message.reply(f'{message.from_user.first_name}, да ты жадина, не хочешь ли взять поменьше?')