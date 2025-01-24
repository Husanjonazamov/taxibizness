# aiogram import
from aiogram.types import Message, ContentType
from aiogram.dispatcher import FSMContext

# kode import 
from loader import dp
from utils import texts, buttons
from states.state import Passenger

# add import
from asyncio import create_task


async def passanger_phone_task(message: Message, state: FSMContext):
    """
    Yo'lovchidan telefon raqamnini olib beruvchi funksiya    
    """
    if message.content_type == ContentType.TEXT:
        phone_number = message.text

    elif message.content_type == ContentType.CONTACT:
        phone_number = message.contact.phone_number

    if phone_number.startswith('+998'):
        if not phone_number.startswith('+'):
            phone_number = '+' + phone_number  
    else:
        if not phone_number.startswith('+'):
            phone_number = '+' + phone_number 

    await state.update_data({
        'phone_number': phone_number
    })
    data = await state.get_data()
    count = data.get('count')
    location = data.get('location')

    await message.answer(
        texts.confirmation_user(
            count=count, 
            location=location,
            phone_number=phone_number
        ), 
        reply_markup=buttons.PASSENGER_CONFIRMATION
    )

    await Passenger.confirmation.set()



@dp.message_handler(content_types=[ContentType.TEXT, ContentType.CONTACT], state=Passenger.phone)
async def passanger_phone(message: Message, state: FSMContext):
    if message.text in [buttons.BACK]:
        await message.answer(texts.PASSENGER_LOCATION_MESSAGE, reply_markup=buttons.LOCATION)
        await Passenger.location.set()    
    else:
        await create_task(passanger_phone_task(message, state))
