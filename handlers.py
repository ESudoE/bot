from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command
from aiogram.utils.markdown import hbold
from config import dp, bot
from keyboard import photos, index, builder




@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")



@dp.message(Command("help"))
async def help_handle(message: types.Message):
    help_text2 = hbold('вот комманды которые может обробатывать бот:\n\n/film_a1 --> фильм уровня сложности английского A1\n\n/film_a2 --> фильм уровня сложности английского A2\n\n/film_b1 --> фильм уровня сложности английского B1\n\n/film_b2 --> фильм уровня сложности английского B2\n\n/film_c1 --> фильм уровня сложности английского C1\n\n/film_c2 --> фильм уровня сложности английского C2')
    await message.answer(parse_mode='HTML',
                         text= f"Привет!{hbold(message.from_user.full_name)}\n <b>это обучающий бот Obuchalochka\n\nПодборка интересных фильмов на английском языке, в которых легко можно понять речь носителей тем самым обогащать свой словарный запас английского с фильмами\n\n</b> "                         
                         )
    await message.answer(text=help_text2)


@dp.message(Command('film'))
async def film_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photos[index]['url'],
                         caption=photos[index]['cap'],
                         reply_markup=builder.as_markup())



@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
