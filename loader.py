# aiogram import
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# add import
from utils.env import BOT_TOKEN
import logging




logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()


BOT_TOKEN = BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode='html')

dp = Dispatcher(bot, storage=storage)