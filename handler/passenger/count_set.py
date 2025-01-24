# aiogram import 
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from states.state import Passenger
from services import getCategory
from utils.createCategory import createCategory

# add import
from asyncio import create_task




async def passerger_count_task(message: Message, state: FSMContext):
    
    """
    Yo'lovchilar sonini olivchi funksiya
    """
    category = getCategory()

    count = message.text

    await state.update_data({
        'count': count
    })
    
    await message.answer(
            texts.PASSENGER_LOCATION_MESSAGE,
            reply_markup=createCategory(category)
        )
    await Passenger.location.set()    

    
@dp.message_handler(content_types=['text'], state=Passenger.count)
async def passerger_count(message: Message, state: FSMContext):
    await create_task(passerger_count_task(message, state))