from aiogram import types
from loader import dp

from scheduler import WeekSchedule


@dp.message_handler(commands="edit")
async def editor(user_message: types.Message):
    # Ask user so he/she understands that the bot expects a number
    await user_message.answer("Какую неделю хочешь расписать?")
