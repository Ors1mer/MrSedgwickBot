from aiogram import types
from bot import dp


@dp.message_handler(commands=["help", "HELP", "h"])
async def send_help(message: types.Message):
    guide = """Чтобы <i>расписать</i> свой график, выбери неделю <del>(начиная с \
текущей)</del>, потом выбери, чем будешь заниматься в каждый из семи дней.

Ты можешь заполнить <span class="tg-spoiler">сколько угодно</span> недель и \
редактировать каждую из них."""
    await message.reply(guide)
