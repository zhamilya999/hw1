from aiogram.utils import executor
from config import bot, dp
from database import bot_db
from handlers import client, callback, extra, admin, fsmAdminMenu
import logging


async def on_startup(_):
    bot_db.sql_create()

fsmAdminMenu.register_handlers_fsmAdminMenu(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
extra.register_hanlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)