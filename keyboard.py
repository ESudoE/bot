from aiogram.utils.keyboard import InlineKeyboardBuilder
from photo_and_cap import photos,photos_article, photos_app
from aiogram.filters import Command
from config import bot, dp
from aiogram import types
from aiogram.types import  CallbackQuery
from aiogram.enums import ParseMode 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram import filters,F


builder = InlineKeyboardBuilder()
# builder.button(text="<--", callback_data='back')
builder.button(text="-->", callback_data="next")
   

index = 0


@dp.callback_query(F.data == 'next')
async def my_callback_foo(query: CallbackQuery):
    global index
    if query.data == 'next':
        index += 1
    # elif query.data == "back":
    #     index -= 1
    # if index < 0:
    #     index = 5
    if index > 5:
        index = 0
    await query.message.edit_media(
        media=types.InputMediaPhoto(
            media=photos[index]['url'],
            caption=photos[index]['cap']
        ),
        reply_markup=builder.as_markup()
    )

 

builder_article = InlineKeyboardBuilder()
builder_article.button(text="-->", callback_data="next_article")
   

index_article = 0 

@dp.callback_query(F.data == 'next_article')
async def my_callback_foo_article(query: CallbackQuery):
    global index_article
    if query.data == 'next_article':
        index_article += 1
    if index_article > 1:
        index_article = 0
    await query.message.edit_media(
        media=types.InputMediaPhoto(
            media=photos_article[index_article]['url'],
            caption=photos_article[index_article]['cap']
        ),
        reply_markup=builder_article.as_markup()
    )

builder_app = InlineKeyboardBuilder()
builder_app.button(text="-->", callback_data="next_app")
   

index_app = 0 

@dp.callback_query(F.data == 'next_app')
async def my_callback_foo_app(query: CallbackQuery):
    global index_app
    if query.data == 'next_app':
        index_app += 1
    if index_app > 2:
        index_app = 0
    await query.message.edit_media(
        media=types.InputMediaPhoto(
            media=photos_app[index_app]['url'],
            caption=photos_app[index_app]['cap']
        ),
        reply_markup=builder_app.as_markup()
    )
