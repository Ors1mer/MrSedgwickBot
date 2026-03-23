from aiogram import types
from loader import dp

from scheduler import WeekSchedule


@dp.message_handler(commands="view")
async def viewer(user_message: types.Message):
    # Ask user so he/she understands that the bot expects a number
    await user_message.answer("Какую неделю хочешь посмотреть?")

    """ TO_FIX
    # Await for a message with number text, then, output the week
    @dp.message_handler()
    async def process_user_answer(user_answer: types.Message):
        week_number = user_answer.text
        if (
            week_number.isdigit()
            or week_number.startswith("-")
            and week_number[1:].isdigit()
        ):
            week_number = int(week_number)
            week = WeekSchedule(date.today() + timedelta(days=7 * (week_number - 1)))
            await user_answer.answer(week.view())
        else:
            pass
    """
