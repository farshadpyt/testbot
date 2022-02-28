from cgitb import text
from random import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
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
👋𝐇𝐞𝐲 {},
𝐈𝐚𝐦 𝐚 𝐒𝐢𝐦𝐩𝐥𝐞 𝐁𝐨𝐭 𝐅𝐨𝐫 𝐅𝐢𝐧𝐝𝐢𝐧𝐠 𝐈𝐃𝐬 𝐢𝐧 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦.. 🔍 🆔
𝐂𝐥𝐢𝐜𝐤 𝐭𝐡𝐞 𝐇𝐞𝐥𝐩 𝐁𝐮𝐭𝐭𝐨𝐧 𝐨𝐫 /help 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧
"""
HELP_MESSAGE = """
<u>× 𝐓𝐡𝐞 𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 𝐈𝐬 𝐓𝐡𝐞 𝐈𝐃 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐌𝐞𝐭𝐡𝐨𝐝</u>
  ✮ 𝐂𝐥𝐢𝐜𝐤 𝐓𝐡𝐞 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐝 𝐁𝐮𝐭𝐭𝐨𝐧 𝐎𝐫 /id 𝐁𝐞𝐥𝐨𝐰 𝐓𝐨 𝐏𝐢𝐜𝐤 𝐘𝐨𝐮𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐝
  ✮ 𝐂𝐥𝐢𝐜𝐤 𝐓𝐡𝐞 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐧𝐟𝐨 𝐁𝐮𝐭𝐭𝐨𝐦 𝐎𝐫 /info 𝐁𝐞𝐥𝐨𝐰 𝐓𝐨 𝐏𝐢𝐜𝐤 𝐔𝐩 𝐘𝐨𝐮𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧
  ✮ 𝐈𝐟 𝐲𝐨𝐮 𝐬𝐞𝐧𝐝 𝐚 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 [𝐮𝐬𝐢𝐧𝐠 𝐭𝐡𝐞 𝐟𝐨𝐫𝐰𝐚𝐫𝐝 𝐭𝐚𝐠] 𝐟𝐫𝐨𝐦 𝐲𝐨𝐮𝐫 [𝐩𝐮𝐛𝐥𝐢𝐜 𝐨𝐫 𝐩𝐫𝐢𝐯𝐚𝐭𝐞] 𝐠𝐫𝐨𝐮𝐩 𝐲𝐨𝐮 𝐰𝐢𝐥𝐥 𝐫𝐞𝐜𝐞𝐢𝐯𝐞 𝐭𝐡𝐞 𝐈𝐃 𝐨𝐟 𝐭𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩
  ✮ 𝐈𝐟 𝐲𝐨𝐮 𝐬𝐞𝐧𝐝 𝐚 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 [𝐮𝐬𝐢𝐧𝐠 𝐭𝐡𝐞 𝐟𝐨𝐫𝐰𝐚𝐫𝐝 𝐭𝐚𝐠] 𝐟𝐫𝐨𝐦 𝐲𝐨𝐮𝐫 [𝐩𝐮𝐛𝐥𝐢𝐜 𝐨𝐫 𝐩𝐫𝐢𝐯𝐚𝐭𝐞] 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐲𝐨𝐮 𝐰𝐢𝐥𝐥 𝐫𝐞𝐜𝐞𝐢𝐯𝐞 𝐭𝐡𝐞 𝐈𝐃 𝐨𝐟 𝐭𝐡𝐚𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥
  ✮ 𝐈𝐟 𝐘𝐨𝐮 𝐍𝐞𝐞𝐝 𝐓𝐡𝐞 𝐈𝐝 𝐎𝐟 𝐀𝐧𝐲 𝐁𝐨𝐭, 𝐒𝐞𝐧𝐝 𝐁𝐨𝐭 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐇𝐞𝐫𝐞 𝐅𝐫𝐨𝐦 𝐓𝐡𝐚𝐭 𝐁𝐨𝐭 [𝐖𝐢𝐭𝐡 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐓𝐚𝐠]
  ✮ 𝐈𝐟 𝐘𝐨𝐮 𝐍𝐞𝐞𝐝 𝐚 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐔𝐬𝐞𝐫 𝐈𝐝, 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐀 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐓𝐨 𝐓𝐡𝐞𝐦 𝐇𝐞𝐫𝐞 [𝐰𝐢𝐭𝐡 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐓𝐚𝐠]
  ✮ 𝐈𝐟 𝐲𝐨𝐮 𝐠𝐢𝐯𝐞 𝐲𝐨𝐮𝐫 𝐫𝐞𝐩𝐥𝐲 /Json 𝐚𝐧𝐲 [𝐦𝐞𝐬𝐬𝐚𝐠𝐞, 𝐟𝐢𝐥𝐞𝐬, 𝐦𝐞𝐝𝐢𝐚, 𝐬𝐭𝐢𝐜𝐤𝐞𝐫𝐬] 𝐲𝐨𝐮 𝐰𝐢𝐥𝐥 𝐠𝐞𝐭 𝐭𝐡𝐞 𝐉𝐬𝐨𝐧 𝐟𝐢𝐥𝐞𝐬 𝐨𝐟 𝐭𝐡𝐨𝐬𝐞 𝐟𝐢𝐥𝐞𝐬
  
  ✮ 𝐈𝐟 𝐲𝐨𝐮 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐠𝐞𝐭 𝐚𝐧 𝐈'𝐝 𝐨𝐟 𝐚 𝐬𝐭𝐢𝐜𝐤𝐞𝐫 𝐩𝐚𝐜𝐤 𝐣𝐮𝐬𝐭 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐬𝐭𝐢𝐜𝐤𝐞𝐫 𝐚𝐧𝐝 𝐫𝐞𝐩𝐥𝐲 𝐢𝐭 𝐰𝐢𝐭𝐡 /stickerid 𝐜𝐨𝐦𝐦𝐚𝐧𝐝 𝐲𝐨𝐮 𝐰𝐨𝐮𝐥𝐝 𝐠𝐞𝐭 𝐢𝐭𝐬 𝐈𝐝.
"""


START_BUTTON = InlineKeyboardMarkup( [[
        InlineKeyboardButton('🗣️OWNER', url='t.me/farshadck'),
        InlineKeyboardButton('📢HELP', callback_data="help"),
        InlineKeyboardButton('📃ABOUT', callback_data="about"),
        ],[
        InlineKeyboardButton('🖥️ INFO 🖥️', callback_data="info")
        ]]
        )
HELP_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐝", callback_data="id"),
       InlineKeyboardButton("𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐧𝐟𝐨", callback_data="info")
       ],[
       InlineKeyboardButton("🏠 𝐇𝐨𝐦𝐞", callback_data="start"),
       InlineKeyboardButton("⬇️ 𝐂𝐥𝐨𝐬𝐞", callback_data="close"),
       InlineKeyboardButton("🤠 𝐀𝐛𝐨𝐮𝐭", callback_data="about")
       ]]
       )

    
@farshad.on_message(filters.private & filters.command(['start']))
async def start(bot, message):
    buttons = [[
        InlineKeyboardButton('🗣️OWNER', url='t.me/farshadck'),
        InlineKeyboardButton('📢HELP', callback_data="help"),
        InlineKeyboardButton('📃ABOUT', callback_data="about"),
    ],[
        InlineKeyboardButton('🖥️ INFO 🖥️', callback_data="info")
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await farshad.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=START_MESSAGE.format(
                message.from_user.first_name),
        parse_mode="html")

@farshad.on_message(filters.private & filters.command(['help']))
async def start(bot, message):
    buttons = [[
        InlineKeyboardButton("🏠 𝐇𝐨𝐦𝐞", callback_data="start"),
        InlineKeyboardButton("⬇️ 𝐂𝐥𝐨𝐬𝐞", callback_data="close"),
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await farshad.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=HELP_MESSAGE.format(
                message.from_user.first_name),
        parse_mode="html")
    
@farshad.on_message(filters.private & filters.forwarded)
async def info(bot, msg):
    if msg.forward_from:
        text = "<u>𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 👀</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<u>🤖 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨</u>"
        else:
            text += "<u>👤𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨</u>"
        text += f'\n\n👨‍💼 𝐍𝐚𝐦𝐞 : {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:
            text += f'\n\n🔗 𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞 : @{msg.forward_from["username"]} \n\n🆔 ID : <code>{msg.forward_from["id"]}</code>'
        else:
            text += f'\n\n🆔 𝐈𝐃 : `{msg.forward_from["id"]}`'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"❌️𝐄𝐫𝐫𝐨𝐫 <b><i>{hidden}</i></b> ❌️𝐄𝐫𝐫𝐨𝐫",
                quote=True,
            )
        else:
            text = f"<u>𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 👀</u>.\n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "<u>📢 𝐂𝐡𝐚𝐧𝐧𝐞𝐥</u>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "<u>🗣️ 𝐆𝐫𝐨𝐮𝐩</u>"
            text += f'\n\n📃 𝐍𝐚𝐦𝐞 {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:
                text += f'\n\n➡️ 𝐅𝐫𝐨𝐦 : @{msg.forward_from_chat["username"]}'
                text += f'\n\n🆔 𝐈𝐃 : `{msg.forward_from_chat["id"]}`'
            else:
                text += f'\n\n🆔 𝐈𝐃 `{msg.forward_from_chat["id"]}`\n\n'
            await msg.reply(text, quote=True)
    
    
@farshad.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**𝐘𝐨𝐮𝐫 𝐬𝐭𝐢𝐜𝐤𝐞𝐫𝐬 𝐢𝐝 𝐢𝐬**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("𝐇𝐦𝐦𝐦 𝐢𝐭'𝐬 𝐧𝐨𝐭 𝐚 𝐬𝐭𝐢𝐜𝐤𝐞𝐫...!!!")
    
    
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
    

@farshad.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "help":
        await msg.message.edit(
            text="text",
            reply_markup=HELP_BUTTON,
            disable_web_page_preview=True
        )
    elif msg.data == "about":
         await msg.message.edit(
             text="about text"
         )
    elif msg.data == "info":
         await msg.message.edit(
             text= f"""
FIRST NAME - {msg.from_user.first_name}
LAST NAME  - {msg.from_user.last_name}
USER NAME  -  @{msg.from_user.username}
id         - {msg.from_user.id}"""
         )
    elif msg.data == "start":
         await msg.message.edit(
             text=START_MESSAGE,
             reply_markup=START_BUTTON,
             disable_web_page_preview=True
         )
    elif msg.data == "close":
          await msg.message.delete()

        

    
    

    
    
    
farshad.run()    
    
    
    
    
    
    
    
    
    
    
  


