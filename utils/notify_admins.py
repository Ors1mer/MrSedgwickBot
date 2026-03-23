import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    """
    Simply notifies admins that the bot is launched
    """
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "The Bot just launched")

        except Exception as err:
            logging.exception(err)
