import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus, ButtonStyle
from pyrogram.errors import MessageNotModified
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)

from PritiMusic.utils.database.autoplay import (
    is_autoplay_group,
    add_autoplay_group,
    remove_autoplay_group,
)
from PritiMusic.utils.decorators import AdminRightsCheck
from config import BANNED_USERS


AUTOPLAY_BANNER = "https://files.catbox.moe/d4yhs6.png"

# 🔥 PREMIUM EMOJIS LIST 🔥
PREMIUM_EMOJIS = [
    "5422831825178206894", 
    "5368324170673489600",
    "5206607081334906820",
    "5206380668048496464"
]

def autoplay_panel_markup(chat_id: int, enabled: bool):
    status = "🟢 𝐄ɴᴀʙʟᴇᴅ" if enabled else "🔴 𝐃ɪsᴀʙʟᴇᴅ"

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "𝐀ᴜᴛᴏ 𝐏ʟᴀʏ 𝐄ɴᴀʙʟᴇ",
                    callback_data=f"AUTOPLAY_ENABLE|{chat_id}",
                    style=ButtonStyle.SUCCESS,
                    icon_custom_emoji_id=random.choice(PREMIUM_EMOJIS)
                ),
                InlineKeyboardButton(
                    "𝐀ᴜᴛᴏ 𝐏ʟᴀʏ 𝐃ɪsᴀʙʟᴇ",
                    callback_data=f"AUTOPLAY_DISABLE|{chat_id}",
                    style=ButtonStyle.DANGER,
                    icon_custom_emoji_id=random.choice(PREMIUM_EMOJIS)
                ),
            ],
            [
                InlineKeyboardButton(
                    f"𝐀ᴜᴛᴏ 𝐏ʟᴀʏ : {status}",
                    callback_data="AUTOPLAY_STATUS",
                    style=ButtonStyle.PRIMARY,
                    icon_custom_emoji_id=random.choice(PREMIUM_EMOJIS)
                )
            ],
        ]
    )


def autoplay_caption(enabled: bool):
    status = "🟢 𝐄ɴᴀʙʟᴇᴅ" if enabled else "🔴 𝐃ɪsᴀʙʟᴇᴅ"

    return f"""
**🎵 𝐀ᴜᴛᴏ 𝐏ʟᴀʏ 𝐒ᴇᴛᴛɪɴɢ𝐬**

➻ 𝐌ᴀɴᴀɢᴇ 𝐀ᴜᴛᴏ 𝐏ʟᴀʏ ғᴇᴀᴛᴜʀᴇ ғᴏʀ ᴛʜɪs ɢʀᴏᴜᴘ.

**✦ 𝐂ᴜʀʀᴇɴᴛ 𝐒ᴛᴀᴛᴜ𝐬**
{status}

➻ 𝐖ʜᴇɴ 𝐀ᴜᴛᴏ 𝐏ʟᴀʏ ɪ𝐬 𝐄ɴᴀʙʟᴇᴅ, ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ
ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴘʟᴀʏ ʀᴇᴄᴏᴍᴍᴇɴᴅᴇᴅ ᴛʀᴀᴄᴋ𝐬
ᴡʜᴇɴ ᴛʜᴇ ǫᴜᴇᴜᴇ ᴇɴᴅ𝐬.

━━━━━━━━━━━━━━━
⚡ 𝐏ᴏᴡᴇʀᴇᴅ ʙʏ ➛ 🎵˹● 𝑻𝑶𝑴 ✘ 𝑱𝑬𝑹𝑹𝒀 𝑴𝑼𝑺𝑰𝑪 ●˼™🎵
"""


@Client.on_message(
    filters.command(["autoplay"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def autoplay_panel(
    client: Client,
    message: Message,
    _,
    chat_id,
):
    enabled = await is_autoplay_group(chat_id)

    await message.reply_photo(
        photo=AUTOPLAY_BANNER,
        caption=autoplay_caption(enabled),
        reply_markup=autoplay_panel_markup(chat_id, enabled),
    )


@Client.on_callback_query(
    filters.regex(r"^AUTOPLAY_(ENABLE|DISABLE)\|") & ~BANNED_USERS
)
async def autoplay_callback(
    client: Client,
    query: CallbackQuery,
):
    action, chat_id = query.data.split("|")
    chat_id = int(chat_id)

    # Admin verification to prevent standard users from toggling the setting
    member = await client.get_chat_member(chat_id, query.from_user.id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return await query.answer("❌ You must be an admin to change this setting!", show_alert=True)

    if action == "AUTOPLAY_ENABLE":
        await add_autoplay_group(chat_id)
        enabled = True

        await query.answer(
            "🟢 𝐀ᴜᴛᴏ 𝐏ʟᴀʏ 𝐄ɴᴀʙʟᴇᴅ",
            show_alert=False,
        )
    else:
        await remove_autoplay_group(chat_id)
        enabled = False

        await query.answer(
            "🔴 𝐀ᴜᴛᴏ 𝐏ʟᴀʏ 𝐃ɪsᴀʙʟᴇᴅ",
            show_alert=False,
        )

    # Prevent crash if the button is clicked but the status is already what they selected
    try:
        await query.message.edit_caption(
            caption=autoplay_caption(enabled),
            reply_markup=autoplay_panel_markup(chat_id, enabled),
        )
    except MessageNotModified:
        pass


@Client.on_callback_query(
    filters.regex("^AUTOPLAY_STATUS$") & ~BANNED_USERS
)
async def autoplay_status(
    client: Client,
    query: CallbackQuery,
):
    await query.answer(
        "⚡ 𝐀ᴜᴛᴏ 𝐏ʟᴀʏ 𝐒ᴛᴀᴛᴜ𝐬",
        show_alert=False,
    )
