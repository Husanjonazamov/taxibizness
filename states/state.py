# aiogram import
from aiogram.dispatcher.filters.state import State, StatesGroup



class Passenger(StatesGroup):
    count = State()
    location = State()
    phone = State()
    confirmation = State()
    
    
class Driver(StatesGroup):
    name = State()
    phone = State()
    
    
     
     
class Mail(StatesGroup):
    location = State()
    phone = State()