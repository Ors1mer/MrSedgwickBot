import logging

from aiogram import executor

from loader import dp
import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


# Configure logging
logging.basicConfig(level=logging.INFO)

async def on_startup(dispatcher):
    # Creating the menu with the list of commands
    await set_default_commands(dispatcher)

    # Sending a message to every admin that the bot is launched
    await on_startup_notify(dispatcher)


# Launching the bot
if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
