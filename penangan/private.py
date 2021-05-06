from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm {Skyzo Music Bot} 🎵

I can play music in your group's voice call🥴. Developed by [Skyzo](https://t.me/SkyzoGanss).

Add me to your group and play music freely guys!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Group Support 🛠", url="https://t.me/skyzomusicbot")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/skyzomusicbot"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/skyzomusicbot"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/JEGroupMusicPlayerBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Skyzo Music Bot Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Devoloper", url="https://t.me/SkyzoGanss")
                ]
            ]
        )
   )


