# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from services import getUser, createUser

# add import
from asyncio import create_task


async def start_handler_task(message: Message, state: FSMContext):
    user_id = message.from_user.id
    firstname = message.from_user.first_name

    print(f"User ID: {user_id}, First Name: {firstname}")

    getuser = getUser(user_id)

    if not getuser:
        user = {
            'user_id': user_id,
            'firstname': firstname
        }
        createUser(user)

    await message.answer(
        texts.START_MESSAGE.format(firstname),
        reply_markup=buttons.START_BUTTON
    )


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    await create_task(start_handler_task(message, state))
