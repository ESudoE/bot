from aiogram.utils.keyboard import InlineKeyboardBuilder
from text import photos
from aiogram.filters import CommandStart, Command
from config import bot, dp
from aiogram import types
from aiogram.types import  CallbackQuery
from aiogram.filters import  Command, command
from aiogram.enums import ParseMode 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
 

builder = InlineKeyboardBuilder()
builder.button(text="<--", callback_data='back')
builder.button(text="-->", callback_data="next")


@dp.message(Command('key'))
async def key_b(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photos[index]['url'],
                         caption=photos[index]['cap'],
                         reply_markup=builder.as_markup())
    
index = 0

@dp.callback_query()
async def my_callback_foo(query: CallbackQuery):
    global index
    if query.data == 'next':
        index += 1
    elif query.data == "back":
        index -= 1
    if index < 0:
        index = 1
    elif index > 1:
        index = 0
    await query.message.edit_media(
        media=types.InputMediaPhoto(
            media=photos[index]['url'],
            caption=photos[index]['cap']
        ),
        reply_markup=builder.as_markup()
    )