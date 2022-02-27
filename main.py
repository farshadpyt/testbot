from cgitb import text
from random import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random
farshad=Client(
    "pyrogram bot",
    bot_token="5211118841:AAGZAOcFQQKsCjBUFpkaHmkqRO-qwVFjPi0",
    api_id="6203583",
    api_hash="b0849a17c7dd35b96938591e3ea1caca"
)

ALL_PIC = [
 "https://telegra.ph/file/e65116508df148b96111a.jpg",
 "https://telegra.ph/file/1d4735f3285e7a2cc5b37.jpg",
 "https://telegra.ph/file/647fee61578929d0089cf.jpg"
]


START_MESSAGE = """
hello {}
"""


@farshad.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text(
        text=START_MESSAGE.format(message.from_user.mention)
    )
    

    
@farshad.on_message(filters.command("info"))    
async def info(bot, message):
    text = f"""
FIRST NAME - {message.from_user.first_name}
LAST NAME  - {message.from_user.last_name}
USER NAME  - {message.from_user.username}
id         - {message.from_user.id}"""
    
    
    
farshad.run()    
    
    
    
    
    
    
    
    
    
    
  


