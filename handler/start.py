# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons

# add import
from asyncio import create_task


async def start_handler_task(message: Message, state: FSMContext):
    firstname = message.from_user.first_name

    await message.answer(
        texts.START_MESSAGE.format(firstname),
        reply_markup=buttons.START_BUTTON
    )


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    await create_task(start_handler_task(message, state))
