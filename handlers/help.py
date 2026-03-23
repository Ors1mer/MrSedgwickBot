from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

guide = """\
/start – basically no need to explain :)
/help – I guess here's the same
/view – check out the schedule for a week. After choosing this option, you \
have to type in a number, i. e. the number of the week. You count it like \
that: the current week - 1, the next one – 2, etc (use negatives for the \
previous weeks). You may input any amount of numbers and I'll show the \
schedule for each one. When you're done - write something different.
/edit – First of all, choose a week. Then fill up the schedule by picking an \
activity from the list. After that, you can edit another week in the same \
way, or end the process by writing something like \"stop\".
"""

@dp.message_handler(CommandHelp())
async def send_help(user_message: types.Message):
    await user_message.answer(guide)
