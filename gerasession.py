from pyrogram import Client

api_id = 26842599
api_hash = "62d75c03edec207bb78f0fa5bbf74984"
bot_token = "6340619689:AAGllQOLspGK0gJYfW9IKtJyxFqhixUmQiY"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

app.run()