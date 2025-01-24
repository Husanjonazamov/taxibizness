# aiogram import
from aiogram.types import Message, ContentType
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from states.state import Driver
from utils.env import ADMIN

# add import
from asyncio import create_task


async def driver_phone_task(message: Message, state: FSMContext):
    """
    Taksichining telefon raqamini oluvchi funksiya
    """
    
    if message.content_type == ContentType.TEXT:
        phone = message.text

    elif message.content_type == ContentType.CONTACT:
        phone = message.contact.phone_number
    
    if not phone.startswith('+'):
        phone = '+' + phone

    await state.update_data({
        'phone': phone
    })
    
    data = await state.get_data()
    name = data.get('name')
    
    username = message.from_user.username
    
    await bot.send_message(
        chat_id=ADMIN,
        text=texts.send_driver_admin(
            name=name,
            username=username,
            phone=phone,
        )
    )
    
    await message.answer(texts.SEND_DRIVER, reply_markup=buttons.BACK_BUTTON)
    await state.finish()    


@dp.message_handler(content_types=[ContentType.TEXT, ContentType.CONTACT], state=Driver.phone)
async def driver_phone(message: Message, state: FSMContext):
    if message.text in [buttons.BACK]:
        await message.answer(texts.DRIVER_NAME, reply_markup=buttons.BACK_BUTTON)
        await Driver.name.set()
    else:
        await create_task(driver_phone_task(message, state))
