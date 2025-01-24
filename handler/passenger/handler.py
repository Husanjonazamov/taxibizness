# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from states.state import Passenger


# add import
from asyncio import create_task




async def passenger_task(message: Message, state: FSMContext):
    
    """
    Yo'lovchilardan zakaz qabul qiluvchi funksiya    
    """
    
    await message.answer(texts.COUNT_MESSAGE, reply_markup=buttons.COUNT_BUTTON)
    
    await Passenger.count.set()
    
    

@dp.message_handler(
        lambda message: message.text.startswith((
            buttons.PASSENGER_MODE,   
        )),
        state='*')
async def passenger(message: Message, state: FSMContext):
    await create_task(passenger_task(message, state))   

