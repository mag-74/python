from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Назад')

# -- main menu --
btnGame = KeyboardButton('Игры')
btnHelp = KeyboardButton('Помощь')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnGame, btnHelp)

# -- game menu --
btnGame1 = KeyboardButton('Игра в конфеты')
btnGame2 = KeyboardButton('Крестики-нолики')
gameMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnGame1, btnGame2, btnMain)