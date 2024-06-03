## Copy Paster Must Give Credit...
## @JARVIS_V2

from telethon import events, Button
from config import X1, SUDO_USERS, CMD_HNDLR as hl

HELP_STRING = (
    "**𖤍 ᴊᴀʀᴠɪs sᴘᴀᴍ ʜᴇʟᴘ ᴍᴇɴᴜ 𖤍**\n\n"
    "» ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ꜰᴏʀ ʜᴇʟᴘ\n"
    "» **ᴅᴇᴠᴇʟᴏᴘᴇʀ**: @Mohitkumar076"
)

HELP_BUTTONS = [
    [Button.inline("• ꜱᴘᴀᴍ •", data="spam"), Button.inline("• ʀᴀɪᴅ •", data="raid")],
    [Button.inline("• ᴇxᴛʀᴀ •", data="extra")],
    [Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/ROYAL_WORLD_84"),
     Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/R_I_S_I_NG")]
]

EXTRA_MSG = (
    f"**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:**\n\n"
    f"𝗢𝘄𝗻𝗲𝗿: **ᴏᴡɴᴇʀ ᴄᴍᴅꜱ**\n"
    f"  1) {hl}ping\n"
    f"  2) {hl}reboot\n"
    f"  3) {hl}sudo <reply to user>  ➪ Owner Cmd\n"
    f"  4) {hl}logs ➪ Owner Cmd\n\n"
    f"𝗘𝗰𝗵𝗼: **ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ**\n"
    f"  1) {hl}echo <reply to user>\n"
    f"  2) {hl}rmecho <reply to user>\n\n"
    f"𝗟𝗲𝗮𝘃𝗲: **ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ**\n"
    f"  1) {hl}leave <group/chat id>\n"
    f"  2) {hl}leave : ᴛʏᴘᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ\n\n"
    f"**@Mohitkumar076**"
)

RAID_MSG = (
    f"**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:**\n\n"
    f"𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.**\n"
    f"  1) {hl}raid <count> <username>\n"
    f"  2) {hl}raid <count> <reply to user>\n\n"
    f"𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**\n"
    f"  1) {hl}rraid <replying to user>\n"
    f"  2) {hl}rraid <username>\n\n"
    f"𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**\n"
    f"  1) {hl}drraid <replying to user>\n"
    f"  2) {hl}drraid <username>\n\n"
    f"𝐌𝐑𝐚𝐢𝐝: **ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**\n"
    f"  1) {hl}mraid <count> <username>\n"
    f"  2) {hl}mraid <count> <reply to user>\n\n"
    f"𝐒𝐑𝐚𝐢𝐝: **ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**\n"
    f"  1) {hl}sraid <count> <username>\n"
    f"  2) {hl}sraid <count> <reply to user>\n\n"
    f"𝐐𝐑𝐚𝐢𝐝: **ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**\n"
    f"  1) {hl}qraid <count> <username>\n"
    f"  2) {hl}qraid <count> <reply to user>\n\n"
    f"**© @Mohitkumar076**"
)

SPAM_MSG = (
    f"**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:**\n\n"
    f"𝗦𝗽𝗮𝗺: **ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ.**\n"
    f"  1) {hl}spam <count> <message to spam>\n"
    f"  2) {hl}spam <count> <replying any message>\n\n"
    f"𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺: **ᴘᴏʀɴᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ.**\n"
    f"  1) {hl}pspam <count>\n\n"
    f"𝗛𝗮𝗻𝗴: **ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇꜱ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ.**\n"
    f"  1) {hl}hang <counter>\n\n"
    f"**© @Mohitkumar076**"
)

def is_sudo_user(user_id):
    return user_id in SUDO_USERS

async def send_help_message(event):
    await event.client.send_file(
        event.chat_id,
        "https://telegra.ph/file/41b903c834a8af32e2281.jpg",
        caption=HELP_STRING,
        buttons=HELP_BUTTONS
    )

async def send_error_message(event, error):
    await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(error)}")

async def handle_help_back(event):
    await event.edit(
        HELP_STRING,
        buttons=HELP_BUTTONS
    )

async def handle_callback_query(event, message, back_button_data):
    await event.edit(
        message,
        buttons=[[Button.inline("< Back", data=back_button_data)],]
    )

async def handle_callback_query_error(event):
    await event.answer("ᴘᴀʜʟᴇ ᴊᴀʀᴠɪs ᴘᴀᴘᴀ sᴇ sᴜᴅᴏ ʟᴇʟᴏ☎️ @Mohitkumar076", cache_time=0, alert=True)

@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if is_sudo_user(event.sender_id):
        try:
            await send_help_message(event)
        except Exception as e:
            await send_error_message(event, e)

@X1.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if is_sudo_user(event.query.user_id):
        await handle_help_back(event)
    else:
        await handle_callback_query_error(event)

@X1.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if is_sudo_user(event.query.user_id):
        await handle_callback_query(event, SPAM_MSG, "help_back")
    else:
        await handle_callback_query_error(event)

@X1.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if is_sudo_user(event.query.user_id):
        await handle_callback_query(event, RAID_MSG, "help_back")
    else:
        await handle_callback_query_error(event)

@X1.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if is_sudo_user(event.query.user_id):
        await handle_callback_query(event, EXTRA_MSG, "help_back")
    else:
        await handle_callback_query_error(event)
