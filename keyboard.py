from aiogram.utils.keyboard import InlineKeyboardBuilder
from photo_and_cap import photos,photos_article, photos_app,photo_level,photo_advice,photo_blogers, photo_podcast
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


builder_level = InlineKeyboardBuilder()
builder_level.button(text="-->", callback_data="next_level")
   

index_level = 0 

@dp.callback_query(F.data == 'next_level')
async def my_callback_foo_level(query: CallbackQuery):
    global index_level
    if query.data == 'next_level':
        index_level += 1
    if index_level > 4:
        index_level = 0
    await query.message.edit_media(
        media=types.InputMediaPhoto(
            media=photo_level[index_level]['url'],
            caption=photo_level[index_level]['cap']
        ),
        reply_markup=builder_level.as_markup()
    )


builder_advice = InlineKeyboardBuilder()
builder_advice.button(text="-->", callback_data="next_advice")
   

index_advice= 0 

@dp.callback_query(F.data == 'next_advice')
async def my_callback_foo_method(query: CallbackQuery):
    global index_advice
    if query.data == 'next_advice':
        index_advice += 1
    if index_advice > 4:
        index_advice = 0
    await query.message.edit_media(
        media=types.InputMediaPhoto(
            media=photo_advice[index_advice]['url'],
            caption=photo_advice[index_advice]['cap']
        ),
        reply_markup=builder_advice.as_markup()
    )


builder_blogers = InlineKeyboardBuilder()
builder_blogers.button(text="-->", callback_data="next_blogers")

index_blogers= 0 

@dp.callback_query(F.data == 'next_blogers')
async def my_callback_foo_method(query: CallbackQuery):
    global index_blogers
    if query.data == 'next_blogers':
        index_blogers += 1
    if index_blogers > 4:
        index_blogers = 0
    await query.message.edit_media(
        media=types.InputMediaPhoto(
            media=photo_blogers[index_blogers]['url'],
            caption=photo_blogers[index_blogers]['cap']
        ),
        reply_markup=builder_blogers.as_markup()
    )


builder_podcast = InlineKeyboardBuilder()
builder_podcast.button(text="-->", callback_data="next_podcast")

index_podcast= 0 

@dp.callback_query(F.data == 'next_podcast')
async def my_callback_foo_podcast(query: CallbackQuery):
    global index_podcast
    if query.data == 'next_podcast':
        index_podcast += 1
    if index_podcast > 4:
        index_podcast = 0
    await query.message.edit_media(
        media=types.InputMediaPhoto(
            media=photo_podcast[index_podcast]['url'],
            caption=photo_podcast[index_podcast]['cap']
        ),
        reply_markup=builder_podcast.as_markup()
    )