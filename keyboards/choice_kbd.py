from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

activities = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Очное 🎓"),
            KeyboardButton(text="Заочное 📚"),
        ],
        [
            KeyboardButton(text="Учёба 🤟"), 
            KeyboardButton(text="Работа 🔥")
        ],
    ],
    resize_keyboard=True,
)
