import logging

from data import config
from aiogram import Bot, Dispatcher, executor, types


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# -------------------------------
# Handlers
# -------------------------------


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    greeting = """Привет! Меня зовут Mr. Sedgwick и я помогу тебе организовать \
твой график."""
    await message.reply(greeting)


@dp.message_handler(commands=["help", "HELP", "h"])
async def send_help(message: types.Message):
    guide = """Чтобы <i>расписать</i> свой график, выбери неделю <del>(начиная с \
текущей)</del>, потом выбери, чем будешь заниматься в каждый из семи дней.

Ты можешь заполнить <span class="tg-spoiler">сколько угодно</span> недель и \
редактировать каждую из них."""
    await message.reply(guide)


@dp.message_handler(commands=["formatting"])
async def send_formatting(message: types.Message):
    text = """<b>bold</b>, <strong>bold</strong>
<i>italic</i>, <em>italic</em>
<u>underline</u>, <ins>underline</ins>
<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>
<span class="tg-spoiler">spoiler</span>, <tg-spoiler>spoiler</tg-spoiler>
<b>bold <i>italic bold <s>italic bold strikethrough <span class="tg-spoiler">italic bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> bold</b>
<a href="http://www.example.com/">inline URL</a>
<a href="tg://user?id=123456789">inline mention of a user</a>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>
<pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>
"""
    await message.answer(text)


# -------------------------------
# Launching the bot
# -------------------------------

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
