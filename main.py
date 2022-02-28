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



    
@farshad.on_message(filters.private & filters.command(['start']))
async def start(bot, message):
    buttons = [[
        InlineKeyboardButton('🗣️Group', url='t.me/mo_tech_Group'),
        InlineKeyboardButton('📢Updates', url='t.me/mo_tech_yt'),
        InlineKeyboardButton('📃Bot List', url='https://t.me/Mo_Tech_YT/176'),
    ],[
        InlineKeyboardButton('🖥️ How To Own 🖥️', url='https://youtu.be/8kS8C9Tyvnc')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await farshad.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=START_MESSAGE.format(
                message.from_user.first_name),
        parse_mode="html")

    
@farshad.on_message(filters.command("info"))    
async def info(bot, msg):
    text = f"""
FIRST NAME - {msg.from_user.first_name}
LAST NAME  - {msg.from_user.last_name}
USER NAME  -  @{msg.from_user.username}
id         - {msg.from_user.id}"""
    await msg.reply_text(text=text)
    
    
@farshad.on_message(filters.group & filters.command("id"))    
async def id(bot, message):
    text = f""" 
TITLE : {message.chat.title}
USER NAME : @{message.chat.username}
ID : {message.chat.id}"""
    await message.reply_text(text=text)

    
    
@farshad.on_message(filters.command("id"))    
async def id(bot, msg):
    text = f"""
FIRST NAME - {msg.from_user.first_name}
LAST NAME  - {msg.from_user.last_name}
USER NAME  -  @{msg.from_user.username}
id         - {msg.from_user.id}"""
    await msg.reply_text(text=text)
    
farshad.run()    
    
    
    
    
    
    
    
    
    
    
  


