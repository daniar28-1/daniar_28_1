import logging
from aiogram.utils import executor
from handlers import admin, clients, callback, extra
from config import dp, bot


clients.register_clients(dp)
callback.register_handlers_callback(dp)
extra.register_extra(dp)
admin.register_handlers_admin(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
