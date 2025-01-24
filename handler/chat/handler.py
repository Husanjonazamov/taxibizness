from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from utils.env import CHANNEL_ID

from asyncio import create_task
import re
import unicodedata


def contains_url(text):
    """
    Matnda URL borligini tekshiruvchi funksiya
    """
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return bool(url_pattern.search(text))


def normalize_text(text):
    text = unicodedata.normalize('NFKD', text) 
    text = ''.join([c for c in text if not unicodedata.combining(c)])  
    return text.lower() 


async def chat_handler_task(message: Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name
    mail = message.text

    mail_normalized = normalize_text(mail)
    group_name = message.chat.username if message.chat.type in ['group', 'supergroup'] else "Gurpa usernamesi topilmadi"


    restricted_words = [
	'avto', 'авто', 'yuramiz', 'юрамиз',
	'joy', 'жой', 'kam', 'кам', 'aktiv', 'актив',
	'oylik', 'ойлик', 'lichka', 'личка',
	'faberlik', 'фаберлик', 'faberlic', 'фаберлик',
	'ishonchli', 'ишончли', 'assalomu alaykum', 'ассалому алайкум',
	'licga', 'личга'
    ]

    for word in restricted_words:
        if word in mail_normalized:
            print(f"Xabar ichida taqiqlangan so‘z bor: {word}")
            return

    if contains_url(mail_normalized):
        print("Xabar ichida URL bor.")
        return

    try:
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=texts.text_to_send(
                group_name=group_name,
                username=username,
                mail=mail,
            ),
            reply_markup=buttons.group_mail_success_admin(user_id)
        )
    except Exception as e:
        print(f"Error sending mail message: {e}")


@dp.message_handler(content_types=['text'], state='*')
async def chat_handler(message: Message, state: FSMContext):
    if message.chat.type in ['group', 'supergroup']:
        await create_task(chat_handler_task(message, state))
