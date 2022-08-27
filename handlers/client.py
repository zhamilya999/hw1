from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
import random
from database.bot_db import sql_command_random

#@dp.message_handler(commands=['meme'])
async def send_meme(message: types.Message):
    list = ["media/i.webp", "media/i(1).webp", "media/i(2).webp", "media/i(3)webp"]
    photo = open(random.choice(list), 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


# @dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Привет! {message.from_user.full_name}")

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


async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await bot.send_message(message.chat.id, "Это команда работает при отваете на сообщение")


async def show_random_user(message: types.Message):
    await sql_command_random(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(start_handler, commands=['meme'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix=['!'])
