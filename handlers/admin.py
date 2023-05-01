from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMINS, bot
from database.bot_db import sql_command_delete

async def pin_handler(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS:  # Закреплять сообщения могут только админы
            await message.answer('Ты не админ!')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение!')
        else:
            await bot.pin_chat_message(message.chat.id,
                                       message.reply_to_message.message_id)
    else:
        await message.answer('Пиши в группу')

async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer('Ты не мой хазяин')
    else:
        users = await sql_command_delete()
        for users in users:
            await message.answer(f'информация о менторе:\n'
                                 f'ID ментора - {users["ID_mentor"]}\n'
                                 f'имя ментора -{users["name"]}\n'
                                 f'напровление - {users["direction"]}\n'
                                 f'сколько лет -{users["age"]}\n'
                                 f'група - {users["group"]} ')
            await users.next()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin_handler, commands=['pin'], commands_prefix='!/')