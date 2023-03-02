import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    text1 = await bot.send_message(msg.chat.id, f"ʜᴇʏ❣️🥀 `{msg.from_user.mention}`, ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ!!")
    await asyncio.sleep(1.5)
    text2 = await text1.edit(f"ᴡᴀɪᴛ ʙᴀʙY✨❣️! ʟᴇᴛ ᴍᴇ ɢᴇᴛ ꜱᴛᴀʀᴛᴇᴅ \nꜱᴏ ᴛʜᴀᴛ ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍʏ ᴘᴏᴡᴇʀ✨❣️🥀")
    await asyncio.sleep(1.5)
    await text2.delete()
    alt = await bot.get_me()
    me2 = alt.mention
    await bot.send_photo(
        chat_id=msg.chat.id,
         photo="https://te.legra.ph/file/f7457547a93f8ea475c2c.jpg",
         caption=f"""**ʜᴇʏ❣️🥀 {msg.from_user.mention},
         
ɪ'ᴍ {me2} ,
ᴀ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ
ᴘᴏᴡᴇʀᴇᴅ ʙʏ :@ScaryNetwork**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url="https://t.me/ScaryServer"),
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/Chat_ixz")
                ]
            ]
        ),
    )
