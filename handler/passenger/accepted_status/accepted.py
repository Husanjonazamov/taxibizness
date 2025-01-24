# aiogram import
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import 
from loader import dp, bot
from utils import buttons, texts

# add import
from asyncio import create_task




async def accepted_task(callback: CallbackQuery, state: FSMContext):
    
    """
    Yo'lovchini qabul qilingani qabar beruvchi funksiya
    """
    
    parts = callback.data.split('_')
    user_id = parts[1] 
    taxi_username = callback.from_user.username

   
    await bot.answer_callback_query(callback.id, text=texts.ACCEPTANCE_PASSENGER.format(taxi_username), show_alert=True)
    


@dp.callback_query_handler(lambda callback_query: callback_query.data and callback_query.data.startswith("accepted_"), state="*")
async def accepted(callback: CallbackQuery, state: FSMContext):
    await create_task(accepted_task(callback, state))
