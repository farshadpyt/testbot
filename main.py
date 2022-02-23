from pyrogram import Client, filters


farshad=Client(
    "pyrogram bot",
    bot_token="5211118841:AAGZAOcFQQKsCjBUFpkaHmkqRO-qwVFjPi0",
    api_id="6203583",
    api_hash="b0849a17c7dd35b96938591e3ea1caca"
)

@farshad.on_message(filter.command("start"))
async def start_message(bot, message):
    await message.reply_text("hi hello")

farshad.run()
