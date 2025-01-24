from environs import Env

env = Env()
env.read_env()

BOT_TOKEN=env('BOT_TOKEN') 
BASE_URL = env('BASE_URL')
ADMIN=env('ADMIN')
CHANNEL_ID=env('CHANNEL_ID')