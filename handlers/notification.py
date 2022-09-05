import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text='Ok')


async def sunday_routine():
    await bot.send_message(chat_id=chat_id, text="Shhh. Its a Sunday...")


async def photo():
    photo = open("media/img.png", "rb")
    await bot.send_photo(chat_id=chat_id, photo=photo, caption="Отсыпайся глупец!!!")


async def scheduler():
    aioschedule.every().saturday.at("00:11").do(sunday_routine)
    aioschedule.every().monday.at("15:17").do(photo)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: "напомни" in word.text)
