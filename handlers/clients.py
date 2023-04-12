from config import bot
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random


async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет хозяин {message.from_user.full_name}!")
    await message.answer("This is an answer method!")
    await message.reply("This is a reply method!")


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="quiz_1_button")
    markup.add(button_1)

    question = "By whom invented Python?"
    answer = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Иди учись",
        open_period=10,
        reply_markup=markup
    )


async def send_meme(message: types.Message):
    something = [
        'smile',
        'fun',
        'funny'
    ]
    random_mem = random.choice(something)

    await bot.send_message(chat_id=message.from_user.id, text=random_mem)


def register_clients(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(send_meme, commands=['mem'])