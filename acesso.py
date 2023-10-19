from pyrogram import Client

app = Client("+5598981071821")

async def main():
    await app.start()
    await app.send_message("me", "Hi!")
    await app.stop()


app.run(main())
