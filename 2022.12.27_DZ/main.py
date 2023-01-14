from commands import dp
from aiogram.utils import executor


async def bot_start(_):
    print('Бот запущен!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=bot_start)