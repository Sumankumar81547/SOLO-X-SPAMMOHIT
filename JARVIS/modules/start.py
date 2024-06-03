## Copy Paster Must Give Credit...
## @JARVIS_V2

from telethon import __version__, events, Button
from config import X1

# Constants
START_BUTTON = [
    [Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/ROYAL_WORLD_84"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/R_I_S_I_NG")
    ],
    [Button.url("• ʀᴇᴘᴏ •", "https://github.com/Sumankumar81547/SOLO-X-SPAMMOHIT")]
]

IMAGE_URL = "https://github.com/doraemon890/JARVIS-X-SPAM/assets/155803358/f30a5777-9823-45d0-9860-342eceadb774"
PYTHON_VERSION = "3.11.3"
JARVIS_VERSION = "M 1.8.31"

async def get_bot_info(event):
    ANNIE = await event.client.get_me()
    bot_name = ANNIE.first_name
    bot_id = ANNIE.id
    return bot_name, bot_id

def create_start_text(bot_name, bot_id, sender_name, sender_id):
    return (
        f"**ʜᴇʏ​ [{sender_name}](tg://user?id={sender_id}),\n\n"
        f"ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n"
        "━━━━━━━━━━━━━━━━━━━\n\n"
        f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [MOHIT](https://t.me/Mohitkumar076)**\n\n"
        f"» **Mohitkumar076 :** `{JARVIS_VERSION}`\n"
        f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{PYTHON_VERSION}`\n"
        f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n"
        "━━━━━━━━━━━━━━━━━"
    )

@X1.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        bot_name, bot_id = await get_bot_info(event)
        start_text = create_start_text(bot_name, bot_id, event.sender.first_name, event.sender.id)
        await event.client.send_file(
            event.chat_id,
            IMAGE_URL,
            caption=start_text,
            buttons=START_BUTTON
        )
