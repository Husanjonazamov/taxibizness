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
    """
    Matnni kichik harflarga va normal shaklga keltirish (diakritik belgilarsiz)
    """
    text = unicodedata.normalize('NFKD', text)
    text = ''.join([c for c in text if not unicodedata.combining(c)])
    return text.lower()


# Taqiqlangan so‘zlar (asl shaklda)
RAW_RESTRICTED_WORDS = [
    'avto', 'авто', 'avtomobil', 'автомобиль', 'mashina', 'машина', 'car',
    'yuramiz', 'юрамиз', 'joy', 'жой', 'kam', 'кам', 'aktiv', 'актив',
    'oylik', 'ойлик', 'lichka', 'личка', 'licga', 'личга',
    'faberlik', 'фаберлик', 'faberlic', 'ishonchli', 'ишончли',
    'assalomu alaykum', 'ассалому алайкум', 'места буш тел', 'юраман',
    'joymiz qoldi', 'жоймиз қолди', 'toshkent shahar ichiga', 'zarur pochta olamiz',
    '❄️❄️❄️❄️❄️❄️',

    # Mashina modellari
    'cobalt', 'cobolt', 'jentra', 'gentra', 'malibu', 'nexia', 'nexia 3', 'spark',
    'tico', 'damas', 'matiz', 'captiva', 'tracker', 'equinox', 'onix', 'tahoe',
    'lacetti', 'orlando', 'ravon', 'chevrolet', 'gm', 'daewoo', 'buick', 'hyundai',
    'kia', 'toyota', 'mazda', 'lexus', 'bmw', 'mers', 'mercedes', 'honda', 'rav4',
    'elantra', 'sonata', 'accent', 'prado', 'camry', 'granta', 'lada', 'vesta',

    # Yangi qo‘shilganlar
    'аеллар', 'багаж', '1та одам почта оламиз', 'всем привет'
]

# Normalize qilingan shaklda so‘zlar
RESTRICTED_WORDS = [normalize_text(w) for w in RAW_RESTRICTED_WORDS]


async def chat_handler_task(message: Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name
    mail = message.text

    # Normalize qilingan matn
    mail_normalized = normalize_text(mail)

    # Guruh nomi
    group_name = message.chat.username if message.chat.type in ['group', 'supergroup'] else "Gurux nomi topilmadi"

    # URL bor-yo‘qligini tekshirish
    if contains_url(mail_normalized):
        print("🚫 Xabar bloklandi: URL mavjud")
        return

    for word in RESTRICTED_WORDS:
        if re.search(rf'\b{re.escape(word)}\b', mail_normalized):
            print(f"🚫 Xabar bloklandi: taqiqlangan so‘z '{word}' aniqlandi.")
            return
        if word in mail_normalized:  # fallback match
            print(f"🚫 Xabar bloklandi: '{word}' topildi.")
            return

    try:
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=texts.text_to_send(
                group_name=group_name,
                username=username,
                mail=mail,
            ),
        )
    except Exception as e:
        print(f"❌ Xatolik: {e}")


@dp.message_handler(content_types=['text'], state='*')
async def chat_handler(message: Message, state: FSMContext):
    if message.chat.type in ['group', 'supergroup']:
        await create_task(chat_handler_task(message, state))
