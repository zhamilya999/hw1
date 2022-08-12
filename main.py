from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from config import bot, dp
import logging
import random

@dp.message_handler(commands=['meme'])
async def send_meme(message: types.Message):
    list = ["media/i.webp", "media/i(1).webp" , "media/i(2).webp", "media/i(3)webp"]
    photo = open(random.choice(list), 'rb')
    await bot.send_photo(message.chat.id, photo=photo)




@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Привет! {message.from_user.full_name}")



@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Какая из этих величин не относится к области информатики?"
    answers = [
        "Килобайт",
        "Мегабит",
        "Теробайт",
        "Киловатт",

    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        open_period=10,
        explanation="Очевидно же",
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "Дискета - это:"
    answers = [
        "Жесткий диск",
        "Лазерный диск",
        "Оптический диск",
        "Гибкий диск",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        open_period=10,
        explanation="Попробуй еще раз!",
        reply_markup=markup
    )


    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        open_period=10,
        explanation="Очевидно же",
    )


@dp.message_handler()
async def echo(message: types.Message):
    try:
        z = int(message.text)
        await bot.send_message(message.from_user.id, z*z)
    except:
        await bot.send_message(message.from_user.id, message.text)





if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)