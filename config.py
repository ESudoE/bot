from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

TOKEN = 'your token'

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

dp = Dispatcher()
