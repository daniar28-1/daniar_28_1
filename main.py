import logging
from aiogram.utils import executor
from config import dp, bot, ADMINS
from handlers import admin, clients, callback, extra, fsm_anketa, schedule
from database.bot_db import sql_creatr


async def on_startup(_):
    await schedule.set_sheduler()
    await bot.send_message(chat_id=ADMINS[0], text='HELOO!')
    sql_creatr()


clients.register_clients(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_anketa.register_handlers_fsm(dp)

# extra.register_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)
