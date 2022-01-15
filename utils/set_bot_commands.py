from aiogram import types


async def set_default_commands(dp):
    """
    This function creates a handsome menu in every chat with a list of specified
    commands
    """
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Greeting"),
            types.BotCommand("help", "Info about bot's capabilities"),
            types.BotCommand("view", "View the schedule of a week"),
            types.BotCommand("edit", "Edit the schedule of a week"),
        ]
    )
