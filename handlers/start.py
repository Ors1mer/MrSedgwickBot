from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def start(user_message: types.Message):
    greeting = """Привет! Меня зовут <b>Mr. Sedgwick</b>. Я помогу тебе \
организовать твой график, сэкономить время и освободить твою голову от лишней \
нагрузки.
Я понимаю четыре команды:
/start – <i>вызвать это сообщение</i>
/help – <i>подробное описание возможностей</i>
/view – <i>посмотреть график на какую-либо неделю</i>
/edit – <i>редактировать график недели</i>"""
    await user_message.answer(greeting)
