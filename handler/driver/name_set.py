# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from states.state import Driver

# add import
from asyncio import create_task




async def driver_name_task(message: Message, state: FSMContext):
    
    """
    Taksichining ismini oluvchi funksiya
    """
    
    name = message.text
    await state.update_data({
        'name': name
    })
    
    await message.answer(texts.PASSENGER_PHONE_MESSAGE, reply_markup=buttons.PHONE)
    
    await Driver.phone.set()
    
    
@dp.message_handler(content_types=['text'], state=Driver.name)
async def driver_name(message: Message, state: FSMContext):
    await create_task(driver_name_task(message, state))
    