from aiogram import types
from loader import dp

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from datetime import date, timedelta
from scheduler import WeekSchedule
from .shared_functions import is_integer


class FormEdit(StatesGroup):
    week_number = State()


@dp.message_handler(commands="edit")
async def editor(user_message: types.Message):
    # Ask user so he/she understands that the bot expects a number
    await user_message.answer("Какую неделю хочешь расписать?")

    await FormEdit.week_number.set()

@dp.message_handler(state=FormEdit.week_number)
async def process_user_answer(user_input: types.Message, state: FSMContext):


    week_number = user_input.text

    if is_integer(week_number):
        week_number = int(week_number)
        week = WeekSchedule(date.today() + timedelta(days=7 * (week_number - 1)))

        bot_message = await user_input.answer(week.view())
    else:
        # the handler stops working
        await user_input.answer("График создан!")
        await state.finish()
