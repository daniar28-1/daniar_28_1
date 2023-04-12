from aiogram import types, Dispatcher
from config import ADMINS, bot


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


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin_handler, commands=['pin'], commands_prefix='!/')