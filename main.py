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

@farshad.on_message(filters.command("leave") & filters.group)
async def leave(bot, message):
    bot.send_message(message.chat id, "Bye I am Leaving This Chat.")
    bot.leave_chat(message.chat.id)
    



@farshad.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption="hello welcome",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("OWNER", url="t.me/farshadck"),
            InlineKeyboardButton("ABOUT", url="t.me/farshadck")
            ],[
            InlineKeyboardButton("OWNER", url="t.me/farshadck")          
            ]]
            )
        )










@farshad.on_message(filters.command("help"))
async def help_message(bot: farshad, message: Message):
    await message.reply_text("help message")

@farshad.on_message(filters.command("about"))
async def about_message(bot, message):
    await message.reply_text("hi hello about")





farshad.run()
