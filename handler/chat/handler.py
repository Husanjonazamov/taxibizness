from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from utils import texts
from utils.env import CHANNEL_ID

from asyncio import create_task
import re
import unicodedata
import string


def contains_url(text):
    """
    Matnda URL borligini tekshiruvchi funksiya
    """
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return bool(url_pattern.search(text))


def normalize_text(text):
    """
    Matnni normal ko‘rinishga keltirish (kirill va lotinni oson taqqoslash uchun)
    - Kirill/lotin harflarini normalize qiladi
    - Diakritik belgilarni olib tashlaydi
    - Kichik harflarga o'tkazadi
    - Punktuatsiyani olib tashlaydi
    """
    text = unicodedata.normalize('NFKD', text)
    text = ''.join([c for c in text if not unicodedata.combining(c)])
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))  # punktuatsiyani olib tashlash
    return text


allowed_phrases = [
    "ketishim kerak", "кетишим керак",
    "pochta bor", "почта бор",
    "taksi kerak", "такси керак",
    "yana taksi kerak", "яна такси керак",
    "olib ketish kerak", "олиб кетиш керак",
    "chiqdim", "чиқдим",
    "manzildan chiqdim", "манзилдан чиқдим",
    "manzilga yetib keling", "манзилга етиб келинг",
    "tayyorman", "тайёрман",
    "tayyor turibman", "тайёр турибман",
    "manzilni ayting", "манзилни айтинг",
    "qayerga borasiz", "қаерга борасиз",
    "taksi bormi", "такси борми",
    "boramiz", "борамиз",
    "kelamiz", "келамиз",
    "birga chiqamiz", "бирга чиқамиз",
    "olib ketasizmi", "олиб кетасизми",
    "chiqib turibman", "чиқиб турибман",
    "qayerdansiz", "қаердансиз",
    "jo‘naymiz", "жўнаймиз",
    "yo‘lga chiqdim", "йўлга чиқдим",
    "ketyapman", "кетяпман",
    "tezro keling", "тезро келинг",
    "taksi yuboring", "такси юбўринг",
    "qani taksi", "қани такси",
    "kutyapman", "кутяпман",
    "yo‘ldaman", "йўлдаман",
    "borishim kerak", "боришим керак",
    "manzilga boraman", "манзилга бораман",
    "qayerda siz", "қаерда сиз",
    "manzildaman", "манзилдаман",
    "kuting", "кутинг",
    "pochta tayyor", "почта тайёр",
    "ketdik", "кетдик",
    "boraylik", "борайлик",
    "ketaylik", "кетаайлик"
]


async def chat_handler_task(message: Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name
    mail = message.text.replace(" ", "  ")

    # Guruhdan kelgan emas, shaxsiydan yozsa chiqarib yuborish
    if message.chat.id == CHANNEL_ID:
        return

    mail_normalized = normalize_text(mail)
    group_name = message.chat.username if message.chat.type in ['group', 'supergroup'] else "Gurpa usernamesi topilmadi"

    # Faqat to‘liq ibora qatnashganmi, substring emas
    if not any(re.search(rf'\b{re.escape(phrase)}\b', mail_normalized) for phrase in allowed_phrases):
        print("✅ Taqiqlangan emas, lekin ruxsat berilgan ibora ham yo‘q.")
        return

    if contains_url(mail_normalized):
        print("🚫 URL aniqlandi, yuborilmaydi.")
        return

    try:
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=texts.text_to_send(
                group_name=group_name,
                username=username,
                mail=mail,
            )
        )
        print("✅ Xabar kanalga yuborildi.")
    except Exception as e:
        print(f"❌ Xatolik: {e}")


@dp.message_handler(content_types=['text'], state='*')
async def chat_handler(message: Message, state: FSMContext):
    if message.chat.type in ['group', 'supergroup']:
        await create_task(chat_handler_task(message, state))
