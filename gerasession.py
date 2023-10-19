from pyrogram import Client
from os import getenv
from dotenv import load_dotenv

load_dotenv()

phone = "+5598981071821"

app = Client(phone, phone_number=phone, api_id=getenv('api_id'), api_hash=getenv('api_hash'))

app.run()
