from aiogram.utils import executor
import logging

from config import dp, bot,ADMINS
from handlers import admin, clients, callback, extra, fsm_anketa,schedule
from database.bot_db import sql_creatr


clients.register_clients(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_anketa.register_handlers_fsm(dp)

extra.register_extra(dp)


async def on_startup(dp):
    await schedule.set_sheduler()
    sql_creatr()
    await bot.send_message(ADMINS[0], 'HELOO!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,)