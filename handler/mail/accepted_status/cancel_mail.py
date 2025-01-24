# aiogram import
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from handler.passenger.accepted_status.cancel_funk import parse_mail_text

# add import 
from asyncio import create_task



async def cancel_mail_task(callback: CallbackQuery, state: FSMContext):
    """
    Taksi Po'chtani bekor qilishi uchun
    """
    parts = callback.data.split('_')
    user_id = parts[1]  
    taxi_id = parts[3]  
    
    
    taxi_id = int(taxi_id)  
    split_data = callback.message.text.split('\n')
    
    username, location, phone = parse_mail_text(split_data)

    if callback.from_user.id == taxi_id:
        await callback.message.delete()

        await bot.send_message(
            chat_id=callback.message.chat.id,
            text=texts.cancel_mail_send_channel(
                username=username,
                location=location,
                phone=phone
            ),
            reply_markup=buttons.mail_success_admin(user_id)  
        )
    else:
        await callback.answer(texts.NOT_MAIL, show_alert=True)


@dp.callback_query_handler(lambda callback_query: callback_query.data and callback_query.data.startswith("mail_cancel_"), state="*")
async def cancel_mail(callback: CallbackQuery, state: FSMContext):
    await create_task(cancel_mail_task(callback, state))
