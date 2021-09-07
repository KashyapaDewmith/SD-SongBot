#kashyapaBOTs <https://telegram.me/IMkashyapaa>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from kashyapa.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from kashyapa import SDbot as app
from kashyapa import LOGGER

pm_start_text = """
Hey [{}](tg://user?id={}), I'm Song Downloader Bot 🎵
�😍 Just send me the song name you want to download.😋
      eg:```/song how you like that black pink```
      
A bot by @IMkashyapaa 
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="Channel😎", url="https://t.me/cgs_officials"
                    ),
                    InlineKeyboardButton(
                        text="Contact me 🔥", url="https://telegram.me/IMkashyapaa"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ Kashyapa Dewmith.")
idle()
