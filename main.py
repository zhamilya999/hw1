from aiogram.utils import executor

from config import dp, URL, bot
from database import bot_db

from handlers import client, callback, extra, admin, fsmAdminMenu, notification, inline
import logging
import asyncio

from decouple import config


async def on_startup(_):
    await bot.set_webhook(URL)
    asyncio.create_task(notification.scheduler())
    bot_db.sql_create()


async def on_shutdown(dp):
    await bot.delete_webhook()


inline.register_inline_handler(dp)
notification.register_handler_notification(dp)
client.register_handlers_client(dp)
fsmAdminMenu.register_handlers_fsmAdminMenu(dp)
callback.register_handlers_callback(dp)
extra.register_hanlers_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path="",
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host='0.0.0.0',
        port=config("PORT", cast=int)
    )