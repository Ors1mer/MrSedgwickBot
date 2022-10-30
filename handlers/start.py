from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

greeting = """Hey! My name is <b>Mr. Sedgwick</b>. I'll help you with \
organizing your schedule, save time and maybe heal your headache.
Contact me with these commands: </start>, </help>, </view>, </edit>"""

@dp.message_handler(CommandStart())
async def start(user_message: types.Message):
    await user_message.answer(greeting)
