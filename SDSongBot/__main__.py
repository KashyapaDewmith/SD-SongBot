#kashyapaBOTs <https://telegram.me/IMkashyapaa>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from kashyapa.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from kashyapa import SDbot as app
from kashyapa import LOGGER

pm_start_text = """
𝐇𝐞𝐲👋 [{}](tg://user?id={}), 𝐈'𝐦 𝐏𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐒𝐨𝐧𝐠 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐛𝐨𝐭 🎵
🎧Just send me the song name you want to download.🎶
      eg:```/song Pretty savage blackpink```
      
𝐀 𝐛𝐨𝐭 𝐛𝐲🌷 @IMkashyapaa 
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
                        text="𝐃𝐞𝐯🌷", url="https://t.me/IMkashyapaa"
                    ),
                    InlineKeyboardButton(
                        text="𝐬𝐮𝐩𝐩𝐨𝐫𝐭 𝐮𝐬🎶", url="https://telegram.me/Cgs_official"
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
