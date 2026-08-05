import random
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus

import config
from PritiMusic.utils.database import get_loop, set_loop
# 🟢 Clone bot ka decorator import
from PritiMusic.cplugin.utils.decorators.admins import AdminRightsCheck 
from config import BANNED_USERS

# ✅ Kurigram Button Style Import
from button import ButtonStyle

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


# 🟢 @Client use kiya hai taki har clone bot isey run kar sake
@Client.on_message(filters.command(["loop", "cloop"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def admins(cli: Client, message: Message, _, chat_id):
    
    if message.from_user.id not in config.SUDOERS:
        try:
            member = await cli.get_chat_member(chat_id, message.from_user.id)
            if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                return await message.reply_text("❌ **Sirf Admins he is command ko use kar sakte hain!**")
        except Exception:
            return await message.reply_text("❌ **Error: Admin rights verify nahi ho paye.**")

    usage = _["admin_17"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
        
    buttons = [
        [ 
            action_btn("✯ ᴄʟᴏɴᴇ ɴᴏᴡ ✯", url="https://t.me/TomXClonerBot", style=ButtonStyle.PRIMARY, use_emoji=True)
        ],
        [
            action_btn("ᴄʟᴏsᴇ ✘", callback_data="close", style=ButtonStyle.DANGER)
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    state = message.text.split(None, 1)[1].strip()
    
    if state.isnumeric():
        state = int(state)
        if 1 <= state <= 10:
            got = await get_loop(chat_id)
            if got != 0:
                state = got + state
            if int(state) > 10:
                state = 10
            await set_loop(chat_id, state)
            return await message.reply_text(
                text=_["admin_18"].format(state, message.from_user.mention),
                reply_markup=reply_markup,
            )
        else:
            return await message.reply_text(usage)
            
    elif state.lower() == "enable":
        await set_loop(chat_id, 10)
        return await message.reply_text(
            text=_["admin_18"].format(state, message.from_user.mention),
            reply_markup=reply_markup,
        )
        
    elif state.lower() == "disable":
        await set_loop(chat_id, 0)
        return await message.reply_text(
            _["admin_19"].format(message.from_user.mention),
            reply_markup=reply_markup,
        )
        
    else:
        return await message.reply_text(usage)
  
