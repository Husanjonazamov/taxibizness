# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import buttons, texts
from states.state import Mail
from handler.start import start_handler

# add import
from asyncio import create_task





async def mail_handler_task(message: Message, state: FSMContext):
    """
    Foydalanuvchi pochtasini qayerdan qayerga yuborishini olib beruvchi funksiya
    """
    
    location = message.text

    await state.update_data({
        'location': location
    })
        
    await message.answer(texts.PASSENGER_PHONE_MESSAGE, reply_markup=buttons.PHONE)
    await Mail.phone.set()
    

@dp.message_handler(content_types=['text'], state=Mail.location)
async def mail_handler(message: Message, state: FSMContext):
    if message.text in [buttons.BACK]:
        await start_handler(message, state)
        await state.finish()
    else:
        await create_task(mail_handler_task(message, state))

