from pyrogram import Client, filters


farshad=Client(
    "pyrogram bot",
    bot_token="bot token",
    api_id="api id",
    api_hash="api hash"
)

@farshad.on_message(filter.command("start"))
async def start_message(bot, message):
    await message.reply_text("hi hello")

farshad.run()
