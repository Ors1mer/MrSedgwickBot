from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from datetime import date, timedelta
from scheduler import WeekSchedule
from .shared_functions import is_integer, append_emoji


class FormEdit(StatesGroup):
    week_number = State()


def get_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Очное 🎓", callback_data="очное"),
                InlineKeyboardButton(text="Заочное 📚", callback_data="заочное"),
            ],
            [
                InlineKeyboardButton(text="Выходной 🤟", callback_data="выходной"),
                InlineKeyboardButton(text="Работа 🔥", callback_data="работа"),
            ],
        ]
    )


@dp.message_handler(commands="edit")
async def editor(user_message: Message):
    # Ask user so he/she understands that the bot expects a number
    await user_message.answer("Какую неделю хочешь расписать?")

    await FormEdit.week_number.set()


@dp.message_handler(state=FormEdit.week_number)
async def process_user_answer(user_input: Message, state: FSMContext):

    week_number = user_input.text

    if is_integer(week_number):
        # Create week's schedule
        week_number = int(week_number)
        week = WeekSchedule(date.today() + timedelta(days=7 * (week_number - 1)))

        # Foolproof: the user shouldn't be able to edit past weeks
        if week_number < 1:
            await user_input.answer("Прошлого не изменить!")
            return

        # Define from which day the editing should start
        # So that the user can't edit past days in the current week
        day = 0
        while week.first_wd + timedelta(days=day) < date.today():
            day += 1

        async with state.proxy() as data:
            data["week"] = week
            data["day"] = day

        # Send the message with schedule
        # On this stage the callback can be called needed amount of times
        await user_input.answer(week.view(), reply_markup=get_keyboard())

    else:
        # The handler stops working
        await user_input.answer("График создан! (Или нет?)")
        await state.finish()


@dp.callback_query_handler(
    text=["очное", "заочное", "выходной", "работа"], state=FormEdit.week_number
)
async def activity_choice(call: CallbackQuery, state: FSMContext):
    indices = {"очное": 0, "заочное": 1, "выходной": 2, "работа": 3}

    # Getting needed variables
    async with state.proxy() as data:
        week = data["week"]
        day = data["day"]

    # Edit the week instance
    activity = call.data
    week.edit(append_emoji(activity, indices[activity]), day)
    # Edit the message with the schedule
    if day < 6:
        await call.message.edit_text(week.view(), reply_markup=get_keyboard())
    else:
        await call.message.edit_text(week.view())

    # Save variables
    async with state.proxy() as data:
        data["week"] = week
        data["day"] = day + 1
    # Tells Telegram that the bot have processed the callback
    await call.answer()
