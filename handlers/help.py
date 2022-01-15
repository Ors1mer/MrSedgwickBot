from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def send_help(user_message: types.Message):
    guide = """Чтобы расписать свой график, выбери неделю (начиная с \
текущей), потом выбери, чем будешь заниматься в каждый из семи дней.
Ты можешь заполнить сколько угодно недель и редактировать каждую из них."""
    await user_message.answer(guide)
