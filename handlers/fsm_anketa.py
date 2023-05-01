from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State,StatesGroup
from config import bot, ADMINS
from database.bot_db import sql_command_inster


class FSMAdnim(StatesGroup):
    ID_mentor = State()
    name_mentor = State()
    direction = State()
    age_mentor = State()
    group = State()
    submit = State()



async def fsm_start(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer('ты не админ')
    else:
        await FSMAdnim.ID_mentor.set()
        await message.answer("ID mentora?")


async def load_ID_mentor(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data["ID_mentor"] = message.text
        print(data)

    await FSMAdnim.next()
    await message.answer("как зовут?")

async def load_name_mentor(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
        print(data)

    await FSMAdnim.next()
    await message.answer('какое направление ? ')


async def load_direction_mentor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["direction"] = message.text
        print(data)

    await FSMAdnim.next()
    await message.answer('сколько лет ? ')


async def load_age_mentor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["age"] = message.text
        print(data)

    await FSMAdnim.next()
    await message.answer('какая группа ? ')

async def load_group_mentor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["group"] = message.text
        print(data)
    await message.answer(f'информация о менторе:\n'
                         f'ID ментора - {data["ID_mentor"]}\n'
                         f'имя ментора -{data["name"]}\n'
                         f'напровление - {data["direction"]}\n'
                         f'сколько лет -{data["age"]}\n'
                         f'група - {data["group"]} ')
    await FSMAdnim.next()
    await message.answer('верно')
async def load_submit(message: types.Message,state: FSMContext):
    if message.text == 'да':
        await sql_command_inster(state)
        await message.answer('Готово!')
        await state.finish()
    elif message.text == 'нет':
        await message.answer('Хорошо')
        await state.finish()

def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=["reg"])
    dp.register_message_handler(load_ID_mentor, state=FSMAdnim.ID_mentor)
    dp.register_message_handler(load_name_mentor, state=FSMAdnim.name_mentor)
    dp.register_message_handler(load_direction_mentor, state=FSMAdnim.direction)
    dp.register_message_handler(load_age_mentor, state=FSMAdnim.age_mentor)
    dp.register_message_handler(load_group_mentor, state=FSMAdnim.group)
    dp.register_message_handler(load_submit, state=FSMAdnim.submit)