import logging

from data import config
from aiogram import Bot, Dispatcher, executor, types

import handlers

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
