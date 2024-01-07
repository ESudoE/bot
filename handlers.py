from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command
from aiogram.utils.markdown import hbold
from config import dp, bot
from text import text_A1,text_C2,text_A2,text_B1,text_B2,text_C1




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



@dp.message(Command('film_a1'))
async def command_english_film_A1(message: types.Message):
    await message.answer_photo(photo='https://cutt.ly/QwHPmqXq', 
                               caption=text_A1)



@dp.message(Command('film_a2'))
async def command_english_film_A2(message: types.Message):
    await message.answer_photo(photo='https://cutt.ly/YwHPWVHB', 
                               caption=text_A2)
    


@dp.message(Command('film_b1'))
async def command_english_film_B1(message: types.Message):
    await message.answer_photo(photo='https://inlnk.ru/70LBal', 
                               caption=text_B1)
    


@dp.message(Command('film_b2'))
async def command_english_film_B2(message: types.Message):
    await message.answer_photo(photo='https://2.bp.blogspot.com/-jUMnJY50Qs8/TXDiDhZN2HI/AAAAAAAACl0/H_aE0VKZaas/s1600/TkeKingsSpeech.jpg', 
                               caption=text_B2)
    


@dp.message(Command('film_c1'))
async def command_english_film_C1(message: types.Message):
    await message.answer_photo(photo='https://th.bing.com/th/id/OIP.2Qb0MJ6WbeCAaWFPNNdf5QHaLH?w=1000&h=1500&rs=1&pid=ImgDetMain', 
                               caption=text_C1)
    


@dp.message(Command('film_c2'))
async def command_english_film_C2(message: types.Message):
    await message.answer_photo(photo='https://inlnk.ru/20YjA9', 
                               caption=text_C2)


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
