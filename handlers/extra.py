from aiogram import types, Dispatcher
from config import bot, dp, ADMIN
import random


#@dp.message_handler()
async def echo(message: types.Message):
    if message.text.startswith('game') and message.from_user.id in ADMIN:
        lst = ['⚽', '🏀', '🎯', '🎳', '🎰', '🎲']
        emoji = random.choice(lst)
        await bot.send_dice(message.chat.id, emoji=emoji)

    else:
        try:
            z = int(message.text)
            await bot.send_message(message.from_user.id, z * z)
        except:
            await bot.send_message(message.from_user.id, message.text)


def register_hanlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)