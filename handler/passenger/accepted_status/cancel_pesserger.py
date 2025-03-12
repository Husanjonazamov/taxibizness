# aiogram import
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from utils.env import BOT_TOKEN
from handler.passenger.accepted_status.cancel_funk import parse_text

# add import 
from asyncio import create_task
import json
import requests

async def cancel_pesserger_task(callback: CallbackQuery, state: FSMContext):
    """
    Taksi Yo'lovchini bekor qilishi uchun
    """
    parts = callback.data.split('_')
    user_id = parts[1]  
    taxi_id = parts[2]  
    
    split_data = callback.message.text.split('\n')
    
    
    username, count, location, phone_number = parse_text(split_data)

  
    if callback.from_user.id == int(taxi_id):
        await callback.message.delete()


        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        caption = texts.cancel_pesserger_admin(
                username=username,
                count=count,
                location=location,
                phone_number=phone_number
            )


        message_data = {
            "chat_id": callback.message.chat.id,
            "text": caption,
            'parse_mode': 'HTML',
            'protect_content': True,
            "reply_markup": json.dumps(buttons.passerger_success_admin(user_id))
        }
        response = requests.post(url, data=message_data)
        

    else:
        await callback.answer(texts.NOT_PESSERGER, show_alert=True)


@dp.callback_query_handler(lambda callback_query: callback_query.data and callback_query.data.startswith("cancel_"), state="*")
async def cancel_pesserger(callback: CallbackQuery, state: FSMContext):
    await create_task(cancel_pesserger_task(callback, state))   
