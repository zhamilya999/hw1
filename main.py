from aiogram.utils import executor
from config import bot, dp
import logging
from handlers import client, callback, extra, admin, fsmAdminMenu

# admin.register_admin_handler(dp)
fsmAdminMenu.register_handlers_fsmAdminMenu(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
extra.register_hanlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)