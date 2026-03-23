import logging

from data import config
from aiogram import Bot, Dispatcher, executor, types

from scheduler import *


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


# -------------------------------
# Handlers
# -------------------------------


@dp.message_handler(commands="start")
async def start(user_message: types.Message):
    greeting = """Привет! Меня зовут <b>Mr. Sedgwick</b>. Я помогу тебе \
организовать твой график, сэкономить время и освободить твою голову от лишней \
нагрузки.

Я понимаю четыре команды:

<code><a href="/start">/start</a></code> – <i>вызвать это сообщение</i>

<a href="/help"><code>/help</code></a> – <i>подробное описание возможностей</i>

<code>/view</code> – <i>посмотреть график на какую-либо неделю</i>

<code>/edit</code> – <i>редактировать график недели</i>"""
    await user_message.answer(greeting)


@dp.message_handler(commands="help")
async def send_help(user_message: types.Message):
    guide = """Чтобы расписать свой график, выбери неделю (начиная с \
текущей), потом выбери, чем будешь заниматься в каждый из семи дней.

Ты можешь заполнить сколько угодно недель и редактировать каждую из них."""
    await user_message.answer(guide)


@dp.message_handler(commands="view")
async def viewer(user_message: types.Message):
    # Ask user so he/she understands that the bot expects a number
    await user_message.answer("Какую неделю хочешь посмотреть?")

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


@dp.message_handler(commands="edit")
async def editor(user_message: types.Message):
    # Ask user so he/she understands that the bot expects a number
    await user_message.answer("Какую неделю хочешь расписать?")


@dp.message_handler(commands="formatting")
async def send_formatting(user_message: types.Message):
    text = """<b>bold</b>, <strong>bold</strong>
<i>italic</i>, <em>italic</em>
<u>underline</u>, <ins>underline</ins>
<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>

<span class="tg-spoiler">spoiler</span>, <tg-spoiler>spoiler</tg-spoiler>
<b>bold <i>italic bold <s>italic bold strikethrough
<span class="tg-spoiler">italic bold strikethrough spoiler</span></s>
<u>underline italic bold</u></i> bold</b>

<a href="http://www.example.com/">inline URL</a>
<a href="tg://user?id=1579532644">inline mention of a user</a>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>
<pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>
"""
    bot_message = await user_message.answer(text)
    await user_message.delete()
    await bot_message.edit_text("The modified one:\n\n" + text)


# -------------------------------
# Launching the bot
# -------------------------------


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
