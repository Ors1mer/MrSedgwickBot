from aiogram import types
from bot import dp


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    greeting = """Привет! Меня зовут Mr. Sedgwick и я помогу тебе организовать \
твой график."""
    await message.reply(greeting)
