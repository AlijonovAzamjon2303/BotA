import asyncio
import logging
import sys
import json

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")



@dp.message(F.text.isdigit())
async def info(message: Message):
    with open("users.json", "r") as file:
        users = json.load(file)
    await message.answer(json.dumps(users.get(message.text, "User topilmadi")))

@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        if "salom" in message.text.lower():
            await message.answer(f"Valeykum assalom {html.bold(message.from_user.full_name)}")
        elif "to'tiqush" in message.text.lower():
            await message.answer("O'zinsan")
        else:
            await message.send_copy(chat_id=message.chat.id)

    except TypeError:
        await message.answer("Nice try")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "main":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())