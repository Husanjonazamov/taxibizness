from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


BE_DRIVER = "🚕 Taksi bo'lish"
PASSENGER_MODE = "🚶 Yo'lovchi"
MAIL = "📬 Po'chta Yuborish"





from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOSHKENTDAN_BESHARIQGA = "Toshkentdan Beshariqga"
BESHARIQDAN_TOSHKENTGA = "Beshariqdan Toshkentga"
BACK = "⬅️ Orqaga"

def create_static_category_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        KeyboardButton(text=TOSHKENTDAN_BESHARIQGA),
        KeyboardButton(text=BESHARIQDAN_TOSHKENTGA)
    )
    keyboard.add(KeyboardButton(text=BACK))
    return keyboard


START_BUTTON = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=MAIL),
        ],
        [
            KeyboardButton(text=BE_DRIVER),
            KeyboardButton(text=PASSENGER_MODE),
        ]
    ],
    resize_keyboard=True
)  



BACK = '⬅️ Ortga'


MAIN_BACK = ReplyKeyboardMarkup(
    keyboard=[
       KeyboardButton(text=BACK) 
    ],
    resize_keyboard=True
)






BASE_BACK = '🔙 Ortga'



BACK_BUTTON = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=BASE_BACK)
        ]
    ],
    resize_keyboard=True
)


ONE_PASSERGER = '1 kishi'
TWO_PASSERGER = '2 kishi'
THREE_PASSERGER = '3 kishi'
FOUR_PASSERGER = '4 kishi'



COUNT_BUTTON = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=ONE_PASSERGER),
            KeyboardButton(text=TWO_PASSERGER)
        ],
        [
            KeyboardButton(text=THREE_PASSERGER),
            KeyboardButton(text=FOUR_PASSERGER)
        ],
        [
            KeyboardButton(text=BASE_BACK)
        ]
    ],
    resize_keyboard=True
)


PHONE_SEND = '📲 Telefon raqamni yuborish'



PHONE = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=PHONE_SEND, request_contact=True)
        ],
        [
            KeyboardButton(text=BACK)
        ]
    ],
    resize_keyboard=True
)

CONFIRMATION = '✅ Tasdiqlash'
CANCEL = '❌ Bekor qilish'


PASSENGER_CONFIRMATION = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=CONFIRMATION)
        ],
        [
            KeyboardButton(text=CANCEL)
        ],
    ],
    resize_keyboard=True
)


def passerger_success_admin(user_id):
    inline_keyboard = {
        "inline_keyboard": [
            [
                {
                    "text": "✅ Qabul qilish", 
                    "callback_data": f'success_{user_id}'
                }
            ]
        ]
    }
    return inline_keyboard
    

def passerger_success_user(user_id, taxi_id, current_taxi_id):
    keyboard = InlineKeyboardMarkup()
    if current_taxi_id == taxi_id:
        keyboard.add(InlineKeyboardButton(text="❌ Bekor qilish", callback_data=f'cancel_{user_id}_{taxi_id}'))
    

    return keyboard



BESH_TASHKENT = 'Beshariq-Toshkent'
TASH_BESHARIQ = 'Toshkent-Beshariq'


LOCATION = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=BESH_TASHKENT),
            KeyboardButton(text=TASH_BESHARIQ),
        ],
        [
            KeyboardButton(text=BACK)
        ]
    ],
    resize_keyboard=True
)





def mail_success_admin(user_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Qabul qilish", 
                    callback_data=f'mail_success_{user_id}' 
                )
            ]
        ]
    )
    
    
def mail_success_user(user_id, taxi_id, current_taxi_id):
    keyboard = InlineKeyboardMarkup()
    if current_taxi_id == taxi_id:
        keyboard.add(InlineKeyboardButton(text="❌ Po'chtani Bekor qilish", callback_data=f'mail_cancel_{user_id}_{taxi_id}'))

    return keyboard



def group_mail_success_admin(user_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Po'chtani Qabul qilish", 
                    callback_data=f'group_mail_success_{user_id}' 
                )
            ]
        ]
    )
    
    
def group_mail_success_user(user_id, taxi_id, current_taxi_id):
    keyboard = InlineKeyboardMarkup()
    if current_taxi_id == taxi_id:
        keyboard.add(InlineKeyboardButton(text="❌ Po'chtani Bekor qilish", callback_data=f'group_mail_cancel_{user_id}_{taxi_id}'))

    return keyboard



BOT_SILKA = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🤖 Botga kirish", url='https://t.me/farbeshbot')
        ]
    ]
)



def bot_button():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚕 Bot orqali buyurtma berish",
                    url="https://t.me/testuchforbot" 
                )
            ]
        ]
    )
    return markup
