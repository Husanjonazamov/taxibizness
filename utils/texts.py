
CHAT = \
"""
👋 Salom, men @farbeshbot! 🤖

💼 Men sizga quyidagi xizmatlarimni taklif qilaman:

🚗 Taksi chaqirish xizmati – Beshariqdan Toshkentgacha yoki aksincha Toshkentdan Beshariqgacha!
📩 Pochta yetkazish – Beshariq va Toshkent ichida Istalgan joyga va istalgan vaqtda pochta jo'natishingiz mumkin.
🔗 Mening xizmatlarimdan foydalanish uchun menga murojaat qiling 
"""


START_MESSAGE = \
"""
<b>
Assalomu alaykum {}!
</b>
"""


COUNT_MESSAGE = \
"""
<b>
Hurmatli Mijoz Yo'lovchilar sonini kiriting!
</b>
"""


PASSENGER_PHONE_MESSAGE = \
"""
Iltimos telefon raqamingizni kiriting yoki pastdagi <b>📲 Telefon raqamni yuborish</b> tugmasini bosing
"""


MAIL_SEND_MESSAGE = \
"""
{} Sizning Xabaringiz taxsilarga yuborildi tez orada siz bilan bog'lanishadi
"""


SUCCES_PESSERGER = \
"""
<b>
✅ Sizning Murojatingiz adminga yuborildi. Tez orada siz bilan bog'lanishadi 
</b>
"""    


SUCCESS_RIDE = \
"""
✅ Tabriklaymiz! siz Yo'lovchini qabul qildingiz
"""

SUCCESS_MAIL = \
"""
✅ Tabriklaymiz! siz Po'chtani qabul qildingiz
"""


ACCEPTANCE_MESSAGE = \
"""
<b>
Sizning arizangizni @{} qabul qilishdi siz bilan bog'lanadi
</b>
"""


ACCEPTANCE_PASSENGER = \
"""
<b>
Bu yo'lovchi allaqachon @{} tomonidan qabul qilngan
</b>
"""



DRIVER_NAME = \
"""
<b>
Ismingizni kiriting
</b>
"""


SEND_DRIVER = \
""" 
<b>
✅ Sizning Arizangiz adminga yuborildi. Tez orada siz bilan bog'lanishadi
</b>
"""


PASSENGER_LOCATION_MESSAGE = \
"""
<b>
Qayerga bormoqchisiz !
</b>
"""



NOT_PESSERGER = \
"""
❌ Bu Yo'lo'vchini faqat qabul qilgan taksi haydovchisi bekor qilishi mumkin.
"""

NOT_MAIL = \
"""
❌ Bu Po'chtani faqat qabul qilgan taksi haydovchisi bekor qilishi mumkin.
"""



MAIL_LOCATION = \
"""
<b>
Pochtangizni qayerga yetkazish kerak 
</b>
"""



MAIL_SUCCESS = \
"""
<b>
✅ Sizning pochtangiz haqidagi malumot adminga yuborildi tez orada siz bilan bo'glanishadi
</b>
"""

def confirmation_user(**kwargs):
    confirmation = ''

    confirmation += f'<b>Malumot:</b>\n\n'
    confirmation += f"<b>Yo'lovchi soni: {kwargs['count']}</b>\n"
    confirmation += f"<b>Manzil: {kwargs['location']}</b>\n"
    confirmation += f'<b>Telefon: <a href="tel:{kwargs["phone_number"]}">{kwargs["phone_number"]}</a></b>\n\n'
    
    return confirmation


def confirmation_admin(**kwargs):
    confirmation = ''

    confirmation += f"<b>Yo'lovchi:</b>\n\n"
    confirmation += f"<b>Username: @{kwargs['username']}</b>\n"
    confirmation += f"<b>Yo'lovchi soni: {kwargs['count']}</b>\n"
    confirmation += f"<b>Manzil: {kwargs['location']}</b>\n"
    confirmation += f'<b>Telefon: <a href="tel:{kwargs["phone_number"]}">{kwargs["phone_number"]}</a></b>\n\n'

    return confirmation
    

def send_driver_admin(**kwargs):
    driver_admin = ''
    
    driver_admin += f"<b>Yangi ariza:</b>\n\n"
    driver_admin += f"<b>ism: {kwargs['name']}</b>\n"
    driver_admin += f"<b>Username: @{kwargs['username']}</b>\n"
    driver_admin += f'<b>Telefon: <a href="tel:{kwargs["phone"]}">{kwargs["phone"]}</a></b>\n'
    
    return driver_admin


def cancel_pesserger_admin(**kwargs):
    confirmation = ''

    confirmation += f"<b>Yo'lovchi:</b>\n\n"
    confirmation += f"<b>Username: {kwargs['username']}</b>\n"
    confirmation += f"<b>Yo'lovchi soni: {kwargs['count']}</b>\n"
    confirmation += f"<b>Manzil: {kwargs['location']}</b>\n"
    confirmation += f'<b>Telefon: <a href="tel:{kwargs["phone_number"]}">{kwargs["phone_number"]}</a></b>\n\n'
    
    return confirmation


def mail_send_channel(**kwargs):
    mail_send = ''
    
    mail_send += f"<b>Po'chta:</b>\n\n"
    mail_send += f"<b>Username: @{kwargs['username']}</b>\n" 
    mail_send += f"<b>Manzil: {kwargs['location']}</b>\n" 
    mail_send += f'<b>Telefon: <a href="tel:{kwargs["phone"]}">{kwargs["phone"]}</a></b>\n' 
    
    return mail_send


def cancel_mail_send_channel(**kwargs):
    mail_send = ''
    
    mail_send += f"<b>Po'chta:</b>\n\n"
    mail_send += f"<b>Username: @{kwargs['username']}</b>\n" 
    mail_send += f"<b>Manzil: {kwargs['location']}</b>\n" 
    mail_send += f'<b>Telefon: <a href="tel:{kwargs["phone"]}">{kwargs["phone"]}</a></b>\n' 
    
    return mail_send


def text_to_send(**kwargs):
    group_mail_send = ''
    
    group_mail_send += f"<b>Yangi xabar:</b>\n\n"
    group_mail_send += f"<b>🏷️ Guruhning usernamesi: @{kwargs['group_name']}</b>\n\n" 
    group_mail_send += f"<b>👤 Foydalanuvchi nomi: @{kwargs['username']}</b>\n\n" 
    group_mail_send += f"<b>📬 Ariza:  {kwargs[ 'mail']}</b>\n\n" 
    
    return group_mail_send


def text_to_send_cancel(**kwargs):
    group_mail_send = ''
    group_mail_send += f"<b>Po'chta:</b>\n\n"
    group_mail_send += f"<b>Username: @{kwargs['username']}</b>\n" 
    group_mail_send += f"<b>Ariza: {kwargs['application']}</b>\n" 
    
    return group_mail_send


PHONE_FORMAT_ERROR = \
"""
Noto'g'ri telefon raqami formati. Iltimos, +998 bilan boshlanadigan telefon raqamini kiriting.
"""


BOT_GROUP_ANONS = \
"""
🚖 Endi taksi chaqirish oson!

🛣 Toshkent ↔ Beshariq yo‘nalishida
📅 Har kuni qatnov
💸 Arzon narx, qulay xizmat

🟢 Bot orqali osongina buyurtma bering va manzilingizga yetib oling!

👉 Hoziroq /start tugmasini bosing!

"""

BOT__USER_ANONS = \
"""
🚖 Endi taksi chaqirish oson!

🛣 Toshkent ↔ Beshariq yo‘nalishida
📅 Har kuni qatnov
💸 Arzon narx, qulay xizmat

🟢 Bot orqali osongina buyurtma bering va manzilingizga yetib oling!

👉 Hoziroq /start tugmasini bosing!

"""