from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.utils.markdown import hbold
from config import dp, bot
from keyboard import photos, index, builder, photos_article, index_article, builder_article, index_app, photos_app, builder_app, index_level,photo_level,builder_level,photo_method,index_method,builder_method
from photo_and_cap import time_table, cap_time_table



@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    await message.answer(f"для навигации введите или нажмите - /navigation")



@dp.message(Command("navigation"))
async def navigation_handle(message: types.Message):
    help_text2 = hbold('Вот все комманды, которые может обробатывать бот:\n\n/start ---> начало работы с ботом\n\n/navigation ---> возможности бота\n\n/film ---> фильмы от А1 до С2\n\n/time_table ---> таблица времён\n\n/article ---> артикли в английском языке\n\n/apps ---> приложения для изучения английского языка\n\n/levels ---> база знаний для уровней английского языка')
    await message.answer(parse_mode='HTML',
                         text= f"Привет!{hbold(message.from_user.full_name)}\n\n<b>это обучающий бот Obuchalochka\n\nПодборка интересных фильмов на английском языке, в которых легко можно понять речь носителей тем самым обогащать свой словарный запас английского с фильмами\n\nТак же вы можете открыть подборку интересных приложений изучения английского языка или выучить таблицу времён от Present Simple  до Future Perfect Continues, или ознокомится с артиклями английского языка\n\nИли вы можете посмотреть базу знаний для каждого уровня ангийского от А1 до С1</b> "                         
                         )
    await message.answer(text=help_text2)


@dp.message(Command('film'))
async def film_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photos[index]['url'],
                         caption=photos[index]['cap'],
                         reply_markup=builder.as_markup())


@dp.message(Command('time_table'))
async def time_table_handle(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=time_table,
                         caption=cap_time_table)
    

@dp.message(Command('article'))
async def article_handler(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photos_article[index_article]["url"],
                         caption=photos_article[index_article]['cap'],
                         reply_markup=builder_article.as_markup())
    
@dp.message(Command('apps'))
async def app_handler(message: types.Message):
    await bot.send_photo(
                         chat_id=message.from_user.id,
                         photo=photos_app[index_app]["url"],
                         caption=photos_app[index_app]["cap"],
                         reply_markup=builder_app.as_markup())


@dp.message(Command('levels'))
async def app_handler(message: types.Message):
    await bot.send_photo(
                         chat_id=message.from_user.id,
                         photo=photo_level[index_level]["url"],
                         caption=photo_level[index_level]["cap"],
                         reply_markup=builder_level.as_markup())


@dp.message(Command('method'))
async def app_handler(message: types.Message):
    await bot.send_photo(
                         chat_id=message.from_user.id,
                         photo=photo_method[index_method]["url"],
                         caption=photo_method[index_method]["cap"],
                         reply_markup=builder_method.as_markup())
