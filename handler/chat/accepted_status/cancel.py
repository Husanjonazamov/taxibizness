# aiogram import
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from handler.passenger.accepted_status.cancel_funk import parse_mail_info

# add import 
from asyncio import create_task



async def cancel_mail_task(callback: CallbackQuery, state: FSMContext):
    """
    Taksi Po'chtani bekor qilishi uchun
    """
    parts = callback.data.split('_')
    user_id = parts[1]  
    taxi_id = int(parts[4])  # taxi_id ni int ga o'zgartirish

    split_data = callback.message.text.split('\n')
    
    username, application = parse_mail_info(split_data)

    if callback.from_user.id == taxi_id:
        await callback.message.delete()
        await bot.send_message(
            chat_id=callback.message.chat.id,
            text=texts.text_to_send_cancel(
                username=username,
                application=application
            ),
            reply_markup=buttons.group_mail_success_admin(user_id)  
        )
    else:
        await callback.answer(texts.NOT_MAIL, show_alert=True)



@dp.callback_query_handler(lambda callback_query: callback_query.data and callback_query.data.startswith("group_mail_cancel_"), state="*")
async def cancel_mail(callback: CallbackQuery, state: FSMContext):
    await create_task(cancel_mail_task(callback, state))
