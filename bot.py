# aiogram import 
from aiogram import executor

# kode import 
from loader import dp, bot
from utils.env import ADMIN
from services import send_daily_message, send_to_groups
import asyncio
import handler


async def on_startup(dispatcher):
    """
    Botni asosiy ishga tushiradigan file
    """
    ADMIN_ID = ADMIN

    asyncio.create_task(send_daily_message(bot))  
    asyncio.create_task(send_to_groups(bot))  
    
    await bot.send_message(ADMIN_ID, 'bot ishga tushdi')


executor.start_polling(dp, skip_updates=False, on_startup=on_startup)