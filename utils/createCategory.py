from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.buttons import BACK


def createCategory(categories):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  
    
    for categories_chunk in chunks(categories, 2): 
        row_buttons = []
        for category in categories_chunk:
            category_button = KeyboardButton(text=category['category'])
            row_buttons.append(category_button)
        keyboard.row(*row_buttons)  

    back_button = KeyboardButton(text=BACK)
    keyboard.add(back_button)  

    return keyboard


def chunks(categories, chunk_size):
    for i in range(0, len(categories), chunk_size):
        yield categories[i:i + chunk_size]
