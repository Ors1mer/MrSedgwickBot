from aiogram import types
from loader import dp

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from datetime import date, timedelta
from scheduler import WeekSchedule
from .shared_functions import is_integer

import pickle


class FormView(StatesGroup):
    week_number = State()


@dp.message_handler(commands="view")
async def viewer(user_message: types.Message):
    # Ask user so he/she understands that the bot expects a number
    await user_message.answer("Какую неделю хочешь посмотреть?")
    # Change state so that process_user_answer could launch
    await FormView.week_number.set()


@dp.message_handler(state=FormView.week_number)
async def process_user_answer(user_input: types.Message, state: FSMContext):
    """
    Await for a message with an integer, then output the week
    This handler will continue to work until the user doesn't send something
    different from integer
    """

    week_number = user_input.text

    if is_integer(week_number):
        week_number = int(week_number)
        week = WeekSchedule(date.today() + timedelta(days=7 * (week_number - 1)))

        # If exists, load the week from db
        user_id = user_input.from_user.id
        schedules = dict()
        try:
            with open(f"db/{user_id}", "rb") as db:
                schedules = pickle.load(db)
                if week.first_wd in schedules.keys():
                    week = schedules[week.first_wd]
        except:  # Excepts EOF and FileNotFound errors
            # Create database file
            open(f"db/{user_id}", "w")

        await user_input.answer(week.view())
    else:
        # the handler stops working
        await user_input.answer("Ты увидел(а) достаточно, принял.")
        await state.finish()
