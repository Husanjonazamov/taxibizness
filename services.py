import requests
from utils.env import BASE_URL





def getAllUsers():
    url = f"{BASE_URL}/users/"
    response = requests.get(url)
    
    if response.status_code == 200:  
        data = response.json()
        return data
    else:
        print(response.status_code)



def createUser(user):
    url = f"{BASE_URL}/users/"
    response = requests.post(url, json=user)
    
    if response.status_code == 201:  
        data = response.json()
        return data
    else:
        print(response.status_code)


def getUser(user_id):
    url = f"{BASE_URL}/users/{user_id}/"
    response = requests.get(url)  
    
    if response.status_code == 200: 
        data = response.json()
        return data
    else:
        print(response.status_code)


def getCategory():
    url = f"{BASE_URL}/category/"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('error')
        
        
        
import asyncio
from utils import texts, buttons, env
from utils.chat_ids import load_chat_ids

async def send_daily_message(bot):
    while True:
        users = getAllUsers()

        for user in users:
            user_id = user['user_id']
            caption = texts.BOT__USER_ANONS
            try:
                await bot.send_photo(
                    chat_id=user_id,
                    photo=env.IMAGE_ID,
                    caption=caption,
                )
            except Exception as e:
                print(f"❌ Xatolik: {user_id} ga yuborilmadi: {e}")
        
        await asyncio.sleep(86400) 
        
        
async def send_to_groups(bot):
    while True:
        group_ids = load_chat_ids()

        for group_id in group_ids:
            captions = texts.BOT_GROUP_ANONS
            
            try:
                await bot.send_photo(
                    chat_id=group_id,
                    photo=env.IMAGE_ID,
                    caption=captions,
                    reply_markup=buttons.bot_button()
                    
                )
            except Exception as e:
                print(f"❌ Guruhga yuborilmadi: {group_id} — {e}")
        
        await asyncio.sleep(18000) 
