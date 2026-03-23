from aiogram import types
from loader import dp

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from datetime import date, timedelta
from scheduler import WeekSchedule

class Form(StatesGroup):
    week_number = State()


@dp.message_handler(commands="view")
async def viewer(user_message: types.Message):
    # Ask user so he/she understands that the bot expects a number
    await user_message.answer("Какую неделю хочешь посмотреть?")
    await Form.week_number.set()

    # Await for a message with number text, then output the week
    @dp.message_handler(state=Form.week_number)
    async def process_user_answer(user_answer: types.Message, state: FSMContext):
        week_number = user_answer.text
        await state.update_data(week_number=week_number)

        if (
            week_number.isdigit()
            or week_number.startswith("-")
            and week_number[1:].isdigit()
        ):
            week_number = int(week_number)
            week = WeekSchedule(date.today() + timedelta(days=7 * (week_number - 1)))
            await user_answer.answer(week.view())
        else:
            await state.finish()
