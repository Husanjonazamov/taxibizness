# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from states.state import Passenger
from utils.env import CHANNEL_ID

# add import
from asyncio import create_task



async def passerger_confirmation_task(message: Message, state: FSMContext):
    
    """
    yo'lovchi malumotlarini gurpaga jo'natadigan funksiya   
    """
    
    
    data = await state.get_data()
    username = message.from_user.username
    phone_number = data.get('phone_number')
    count = data.get('count') 
    location = data.get('location') 
     
     
    user_id = message.from_user.id
    
    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=texts.confirmation_admin(
            username=username,
            count=count,
            location=location,
            phone_number=phone_number
        ),
        reply_markup=buttons.passerger_success_admin(user_id)
    )
    
    await state.update_data(
        username=username,
        count=count,
        location=location,
        phone_number=phone_number
    )

    
    await message.answer(texts.SUCCES_PESSERGER, reply_markup=buttons.BACK_BUTTON)
    
    await state.finish()
    
    
@dp.message_handler(
        lambda message: message.text.startswith((
            buttons.CONFIRMATION,   
        )),
        state='*')
async def passerger_confirmation(message: Message, state: FSMContext):
    await create_task(passerger_confirmation_task(message, state))
    
    
    
