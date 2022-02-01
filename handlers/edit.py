from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from datetime import date, timedelta
from scheduler import WeekSchedule
from .shared_functions import is_integer, append_emoji

import pickle

class FormEdit(StatesGroup):
    week_number = State()


def get_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Очное 🎓", callback_data="очное"),
                InlineKeyboardButton(text="Дистанционное 📚", callback_data="дистанционное"),
            ],
            [
                InlineKeyboardButton(text="Выходной 🤟", callback_data="выходной"),
                InlineKeyboardButton(text="Работа 🔥", callback_data="работа"),
            ],
        ]
    )


@dp.message_handler(commands="edit")
async def editor(user_message: Message, state: FSMContext):
    # Ask user so he/she understands that the bot expects a number
    await user_message.answer("Какую неделю хочешь расписать?")
    
    
    await FormEdit.week_number.set()


@dp.message_handler(state=FormEdit.week_number)
async def process_user_answer(user_input: Message, state: FSMContext):

    week_number = user_input.text

    if is_integer(week_number):
        # --- Create week's schedule ---
        # Creating pure instance
        week_number = int(week_number)
        week = WeekSchedule(date.today() + timedelta(days=7 * (week_number - 1)))

        # If exists, load the week from db
        user_id = user_input.from_user.id
        schedules = dict()
        try:
            with  open(f"db/{user_id}", "rb") as db:
               schedules = pickle.load(db)
               if week.first_wd in schedules.keys():
                    week = schedules[week.first_wd]
        except:
            # Create database file
            open(f"db/{user_id}", 'w')

        # --- Skip past days ---
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
            data["user_id"] = user_id
            data["schedules"] = schedules

        # --- Send message ---
        # On this stage the callback can be called needed amount of times
        await user_input.answer(week.view(), reply_markup=get_keyboard())


    else:
        # The handler stops working
        await user_input.answer("График создан! (Или нет?)")
        await state.finish()


@dp.callback_query_handler(
    text=["очное", "дистанционное", "выходной", "работа"], state=FormEdit.week_number
)
async def activity_choice(call: CallbackQuery, state: FSMContext):
    indices = {"очное": 0,
               "дистанционное": 1,
               "заочное": 1,
               "выходной": 2,
               "работа": 3}

    # Getting needed variables
    async with state.proxy() as data:
        week = data["week"]
        day = data["day"]
        user_id = data["user_id"]
        schedules = data["schedules"]

    # Edit the week instance
    activity = call.data
    week.edit(append_emoji(activity, indices[activity]), day)
    # Edit the message with the schedule
    if day < 6:
        try:
            await call.message.edit_text(week.view(), reply_markup=get_keyboard())
        except: # Intended to handle MessageNotModified exception
            pass
    else:
        try:
            await call.message.edit_text(week.view())
        except:
            pass
        # Save the modified week into db
        with open(f"db/{user_id}", "wb") as db:
            schedules[week.first_wd] = week
            pickle.dump(schedules, db)

    # Save variables
    async with state.proxy() as data:
        data["week"] = week
        data["day"] = day + 1
    # Tells Telegram that the bot have processed the callback
    await call.answer()
