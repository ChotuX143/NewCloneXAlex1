import random
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus

import config
from PritiMusic import app
from PritiMusic.core.call import Lucky
from PritiMusic.utils.database import is_music_playing, music_off
from PritiMusic.utils.decorators import AdminRightsCheck # 🟢 Shukla style import
from config import BANNED_USERS

# ✅ Kurigram Button Style Import
from button import ButtonStyle

# ==========================================
# 🔥 PREMIUM EMOJIS & SMART BUTTON HELPER
# ==========================================
PREMIUM_EMOJIS = [
    "5422831825178206894", 
    "5368324170673489600",
    "5206607081334906820",
    "5206380668048496464"
]

def action_btn(text, callback_data=None, url=None, style=ButtonStyle.PRIMARY, use_emoji=False):
    kwargs = {"text": text, "style": style}
    if callback_data: 
        kwargs["callback_data"] = callback_data
    if url: 
        kwargs["url"] = url
    if use_emoji: 
        kwargs["icon_custom_emoji_id"] = random.choice(PREMIUM_EMOJIS)
    return InlineKeyboardButton(**kwargs)

# ==========================================
# 🛑 PAUSE COMMAND EXECUTION
# ==========================================

@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck 
async def pause_admin(cli, message: Message, _, chat_id):
    
    # 🟢 BULLETPROOF ADMIN CHECK (Double Verification)
    if message.from_user.id not in config.SUDOERS:
        try:
            member = await cli.get_chat_member(chat_id, message.from_user.id)
            if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                return await message.reply_text("❌ **Sirf Admins he is command ko use kar sakte hain!**")
        except Exception:
            return await message.reply_text("❌ **Error: Admin rights verify nahi ho paye.**")

    # 🟢 CHECK KARO KI KYA MUSIC CHAL BHI RAHA HAI?
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])

    # 1. Database mein music off mark karein
    await music_off(chat_id)
    
    # 2. Call module ka use karke stream pause karein
    await Lucky.pause_stream(chat_id)

    # 3. Inline Buttons setup with Kurigram Styles
    buttons = [
        [
            action_btn("ʀᴇsᴜᴍᴇ ▷", callback_data=f"ADMIN Resume|{chat_id}", style=ButtonStyle.SUCCESS),
            action_btn("ʀᴇᴘʟᴀʏ ↺", callback_data=f"ADMIN Replay|{chat_id}", style=ButtonStyle.PRIMARY),
        ],
        [ 
            action_btn("✯ ᴄʟᴏɴᴇ ɴᴏᴡ ✯", url="https://t.me/TomXClonerBot", style=ButtonStyle.PRIMARY, use_emoji=True)
        ],
    ]

    # 4. Reply message
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
    
