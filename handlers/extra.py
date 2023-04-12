from config import bot
from aiogram import Dispatcher, types
from random import choice


async def echo_message(message: types.Message):
    try:
        number = int(message.text)
        result = number ** 2
        await bot.send_message(chat_id=message.from_user.id, text=result)
    except ValueError:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)

    if message.text.lower() == 'game':
        a = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
        random = choice(a)
        await bot.send_dice(message.from_user.id, emoji=random)


def register_extra(dp: Dispatcher):
    dp.register_message_handler(echo_message)
