from pyrogram import Client, filters
from pyrogram.types import Message

farshad=Client(
    "pyrogram bot",
    bot_token="5211118841:AAGZAOcFQQKsCjBUFpkaHmkqRO-qwVFjPi0",
    api_id="6203583",
    api_hash="b0849a17c7dd35b96938591e3ea1caca"
)

@farshad.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text("hi hello")

@farshad.on_message(filters.command("help"))
async def help_message(bot: farshad, message: Message):
    await message.reply_text("help message")

@farshad.on_message(filters.command("about"))
async def about_message(bot, message):
    await message.reply_text("hi hello about")





farshad.run()
