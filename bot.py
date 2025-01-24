# aiogram import 
from aiogram import executor

# kode import 
from loader import dp, bot
from utils.env import ADMIN
import handler



async def on_startup(dispatcher):
    
    """
    Botni asosiy ishga tushiradigan file
    """
    
    ADMIN_ID = ADMIN

    await bot.send_message(ADMIN_ID, 'bot ishga tushdi')


executor.start_polling(dp, skip_updates=False, on_startup=on_startup)