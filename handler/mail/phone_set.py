# aiogram import
from aiogram.types import Message, ContentType
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import buttons, texts
from utils.env import CHANNEL_ID
from states.state import Mail

# add import
from asyncio import create_task


async def mail_phone_task(message: Message, state: FSMContext):
    """
    Foydalanuvchi pochtasini qayerdan qayerga yuborishini olib beruvchi funksiya
    """
    
    user_id = message.from_user.id
    
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
    username = message.from_user.username
    location = data.get('location')
    
    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=texts.mail_send_channel(
            username=username,
            location=location,
            phone=phone
        ),
        reply_markup=buttons.mail_success_admin(user_id)
    )
        
    await message.answer(texts.MAIL_SUCCESS, reply_markup=buttons.BACK_BUTTON)
    await state.finish()
    


@dp.message_handler(content_types=[ContentType.TEXT, ContentType.CONTACT], state=Mail.phone)
async def mail_phone(message: Message, state: FSMContext):
    if message.text in [buttons.BACK]:
        await message.answer(texts.MAIL_LOCATION, reply_markup=buttons.LOCATION)
        await Mail.location.set() 
    else:
        await create_task(mail_phone_task(message, state))
