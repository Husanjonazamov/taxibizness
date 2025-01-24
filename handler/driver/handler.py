# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from states.state import Driver

# add import
from asyncio import create_task

async def driver_handler_task(message: Message, state: FSMContext):
    
    """
    Taksi bo'lmoqchi bo'lganlarni arizasini qabul qiluvchi funksiya
    """
    
    await message.answer(texts.DRIVER_NAME, reply_markup=buttons.BACK_BUTTON)

    await Driver.name.set()

@dp.message_handler(
        lambda message: message.text.startswith((
            buttons.BE_DRIVER,   
        )),
        state='*')
async def driver_handler(message: Message, state: FSMContext):
    await create_task(driver_handler_task(message, state))
    