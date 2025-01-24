# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from handler.start import start_handler

# add import
from asyncio import create_task





async def back_task(message: Message, state: FSMContext):
    
    """
    asosiy ortga qaytish funksiyasi
    """

    await start_handler(message, state)
    await state.finish()

    
@dp.message_handler(
        lambda message: message.text.startswith((
            buttons.BASE_BACK,   
        )),
        state='*')
async def back(message: Message, state: FSMContext):
    await create_task(back_task(message, state))
    



