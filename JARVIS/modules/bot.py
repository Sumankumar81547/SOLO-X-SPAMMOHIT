## Copy Paster Must Give Credit...
## @JARVIS_V2

import sys
import heroku3
from os import execl, getenv
from datetime import datetime
from telethon import events, Button
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from config import X1, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl

REQUIRED_CHANNELS = ["ROYAL_WORLD_84", "R_I_S_I_NG"]

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(event):
    if event.sender_id in SUDO_USERS:
        start = datetime.now()
        reply_message = await event.reply("❄️")
        end = datetime.now()
        ping_time = (end - start).microseconds / 1000
        await reply_message.edit(f"[𝗠𝗢𝗛𝗜𝗧 𝐈𝐒 𝐑𝐄𝐀𝐃𝐘 𝐓𝐎 𝐅𝐔𝐂𝐊 𝐇𝐀𝐓𝐄𝐑𝐒 🥀](https://t.me/R_I_S_I_NG)🤖\n» `{ping_time} ᴍꜱ`")
    else:
        await prompt_join_channels(event)

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(event):
    if event.sender_id in SUDO_USERS:
        await event.reply("`ʙᴏᴛ ɪs ʀᴇsᴛᴀʀᴛɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ`")
        try:
            await X1.disconnect()
        except Exception:
            pass
        execl(sys.executable, sys.executable, *sys.argv)
    else:
        await prompt_join_channels(event)

@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        await manage_sudo_users(event, add=True)
    elif event.sender_id in SUDO_USERS:
        await event.reply("ᴏɴʟʏ ᴊᴀʀᴠɪs ᴄᴀɴ ᴀᴅᴅ sᴜᴅᴏ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ʙʏ .ɢᴇᴛsᴜᴅᴏ")
    else:
        await prompt_join_channels(event)

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
async def removesudo(event):
    if event.sender_id == OWNER_ID:
        await manage_sudo_users(event, add=False)
    else:
        await event.reply("ᴏɴʟʏ ᴊᴀʀᴠɪs ᴄᴀɴ ʀᴇᴍᴏᴠᴇ sᴜᴅᴏ ᴜsᴇʀs")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
async def show_sudo_users(event):
    if event.sender_id == OWNER_ID:
        sudo_users_list = "sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ:\n" + "\n".join(f"- {user_id}" for user_id in SUDO_USERS)
        await event.reply(sudo_users_list)
    else:
        await event.reply("ᴛʜɪs ғᴜɴᴄᴛɪᴏɴ ᴄᴀɴ ᴏɴʟʏ ᴘᴇʀғᴏʀᴍ ʙʏ ᴊᴀʀᴠɪs")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%saddmultisudo(?: |$)(.*)" % hl))
async def addmultisudo(event):
    if event.sender_id == OWNER_ID:
        await manage_multiple_sudo_users(event)
    elif event.sender_id in SUDO_USERS:
        await event.reply("ᴏɴʟʏ ᴊᴀʀᴠɪs ᴄᴀɴ ᴀᴅᴅ ᴍᴜʟᴛɪsᴜᴅᴏ ᴜsᴇʀs ᴀᴛ ᴀ ᴛɪᴍᴇ.")
    else:
        await prompt_join_channels(event)

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sgetsudo(?: |$)(.*)" % hl))
async def getsudo(event):
    if event.sender_id not in SUDO_USERS:
        for channel in REQUIRED_CHANNELS:
            try:
                participants = await X1(GetParticipantsRequest(
                    channel=channel,
                    filter=ChannelParticipantsSearch(''),
                    offset=0,
                    limit=100,
                    hash=0
                ))
                if not any(participant.id == event.sender_id for participant in participants.users):
                    await prompt_join_channels(event)
                    return
            except Exception as ex:
                await event.reply(f"ᴇʀʀᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇᴍʙᴇʀsʜɪᴘ ғᴏʀ {channel}: {ex}")
                return
        await manage_sudo_users(event, add=True)
    else:
        await event.reply("ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ʜᴀᴠᴇ sᴜᴅᴏ ᴘʀɪᴠɪʟʟᴇɢᴇs")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sverify(?: |$)(.*)" % hl))
async def verify(event):
    if await verify_membership(event):
        await manage_sudo_users(event, add=True)
        await event.reply("ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴠᴇʀɪғɪᴇᴅ ᴀɴᴅ ᴀᴜᴛʜᴏʀɪsᴇᴅ ғᴏʀ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ")
    else:
        await prompt_join_channels(event)

async def manage_sudo_users(event, add):
    heroku = heroku3.from_key(HEROKU_API_KEY)
    sudousers = getenv("SUDO_USERS", default="")
    target = str(event.sender_id)

    if HEROKU_APP_NAME:
        app = heroku.app(HEROKU_APP_NAME)
    else:
        await event.reply("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
        return

    heroku_var = app.config()
    if add:
        if target in sudousers.split():
            await event.reply("ᴛʜɪs ɢᴜʏ ɪs ᴀʟʀᴇᴀᴅʏ ɪɴ ᴛʜᴇ sᴜᴅᴏ ᴜsᴇʀ ʟɪsᴛ.")
        else:
            new_sudo_users = f"{sudousers} {target}".strip()
            heroku_var["SUDO_USERS"] = new_sudo_users
            await event.reply(f"ᴀᴅᴅᴇᴅ ɴᴇᴡ sᴜᴅᴏ ᴜsᴇʀs: `{target}`. ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ.")
    else:
        if target not in sudousers.split():
            await event.reply("ᴜsᴇʀ ɪɴ ɴᴏᴛ ɪs sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ.")
        else:
            new_sudo_users = " ".join(user for user in sudousers.split() if user != target)
            heroku_var["SUDO_USERS"] = new_sudo_users
            await event.reply(f"ʀᴇᴍᴏᴠɪɴɢ ᴀʟʟ sᴜᴅᴏ ᴘᴏᴡᴇʀs: `{target}`")

async def manage_multiple_sudo_users(event):
    heroku = heroku3.from_key(HEROKU_API_KEY)
    sudousers = getenv("SUDO_USERS", default="")
    if HEROKU_APP_NAME:
        app = heroku.app(HEROKU_APP_NAME)
    else:
        await event.reply("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
        return

    heroku_var = app.config()
    try:
        target_ids = [str(int(x)) for x in event.pattern_match.group(1).split()]
    except ValueError:
        await event.reply("Error processing the user IDs.")
        return

    new_sudo_users = set(sudousers.split())
    new_sudo_users.update(target_ids)
    heroku_var["SUDO_USERS"] = " ".join(new_sudo_users)
    await event.reply(f"ᴀᴅᴅᴇᴅ {len(target_ids)} ɴᴇᴡ sᴜᴅᴏ ᴜsᴇʀs ɪɴ ᴛʜᴇ ʟɪsᴛ.")

async def prompt_join_channels(event):
    buttons = [
        [Button.url("ᴊᴀʀᴠɪs sᴜᴘᴘᴏʀᴛ", "https://t.me/ROYAL_WORLD_84")],
        [Button.url("sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", "https://t.me/R_I_S_I_NG")],
        [Button.inline("ᴠᴇʀɪғʏ ✅", b"verify_membership")]
    ]
    await event.reply("ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ, ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴠᴀʀs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ:", buttons=buttons)

@X1.on(events.CallbackQuery(data=b"verify_membership"))
async def verify_membership(event):
    if await verify_membership(event):
        await manage_sudo_users(event, add=True)
        await event.reply("ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴠᴇʀɪғɪᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ✅\nᴀᴅᴅᴇᴅʏᴏᴜ ɪɴ sᴜᴅᴏ ᴜsᴇʀs!")
    else:
        await prompt_join_channels(event)

async def verify_membership(event):
    for channel in REQUIRED_CHANNELS:
        try:
            participants = await X1(GetParticipantsRequest(
                channel=channel,
                filter=ChannelParticipantsSearch(''),
                offset=0,
                limit=100,
                hash=0
            ))
            if not any(participant.id == event.sender_id for participant in participants.users):
                return False
        except Exception as ex:
            await event.reply(f"Error checking membership for {channel}: {ex}")
            return False
    return True
