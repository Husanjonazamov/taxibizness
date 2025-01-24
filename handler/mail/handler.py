# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import buttons, texts
from states.state import Mail
from services import getCategory
from utils.createCategory import createCategory

# add import
from asyncio import create_task





async def mail_handler_task(message: Message, state: FSMContext):
    """
    Foydalanuvchilar pochta sini yuboradigan funksiya
    """
    
    category = getCategory()
    
    await message.answer(
            texts.MAIL_LOCATION,
            reply_markup=createCategory(category)
        )
    await Mail.location.set()
    
    
@dp.message_handler(
        lambda message: message.text.startswith((
            buttons.MAIL,   
        )),
        state='*')
async def mail_handler(message: Message, state: FSMContext):
    await create_task(mail_handler_task(message, state))

