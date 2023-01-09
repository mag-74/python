# Создать телеграм-бота на базе библиотеки AIOgram для игры в "Конфетки" против бота

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5913421930:AAF-B02jczWruRigHniNUtaTFoqb8TRe-PU").build()
print('Что-то сделал!')

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("game1", game1_command))
app.add_handler(CommandHandler("game2", game2_command))

app.run_polling()