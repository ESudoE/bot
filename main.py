import asyncio
import logging
from os import getenv

from config import dp, bot
from aiogram import Dispatcher, types, Bot
from aiogram.enums import ParseMode
import handlers

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())