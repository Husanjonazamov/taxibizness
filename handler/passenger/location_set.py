# aiogram import 
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from states.state import Passenger


# add import
from asyncio import create_task




async def passerger_count_task(message: Message, state: FSMContext):
    
    """
    Yo'lovchilar sonini olivchi funksiya
    """
    
    location = message.text

    await state.update_data({
        'location': location
    })
    
    await message.answer(texts.PASSENGER_PHONE_MESSAGE, reply_markup=buttons.PHONE)
    
    await Passenger.phone.set()    

    
@dp.message_handler(content_types=['text'], state=Passenger.location)
async def passerger_count(message: Message, state: FSMContext):
    if message.text in [buttons.BACK]:
        await message.answer(texts.COUNT_MESSAGE, reply_markup=buttons.COUNT_BUTTON)
        await Passenger.count.set()
    else:
        await create_task(passerger_count_task(message, state))