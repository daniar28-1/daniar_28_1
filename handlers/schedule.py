import datetime

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import Crontrigger

from database.bot_db import sql_command_all_uses
from config import bot



async def go_get_some_rest(bot: Bot):
    users = await sql_command_all_uses()
    for user in users:
        await bot.send_message(users[0], f'Привет {user[-1]}/nПора отдыхыть')


async def set_sheduler():
    sheduler = AsyncIOScheduler(timezone='Asia/Bihkek')

    sheduler.add_job(
        go_get_some_rest,
        kwargs={'bot': bot},
        trigger=Crontrigger(
            day_of_week=6,
            start_date=datetime.datetime.now()
        )
    )

    scheduler.start()