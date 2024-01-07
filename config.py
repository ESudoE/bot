from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

TOKEN = '6419671109:AAEYorkU3WcjHdHrNgv96pQ58HHmiT4nj8c'

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

dp = Dispatcher()