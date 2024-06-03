## Copy Paster Must Give Credit...
## @JARVIS_V2

import logging
from telethon import TelegramClient
from os import getenv
from JARVIS.data import FRIDAY

# Set up logging configuration
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# Constants required for JARVIS bots
API_ID = 29195387
API_HASH = "2f13b458072162ffcfce138df44061b3"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
BOT_TOKEN = getenv("BOT_TOKEN", default=None)
MONGO_DB_URI = getenv("MONGO_DB_URI")

# Set up sudo users
SUDO_USERS = list(map(int, getenv("SUDO_USERS", default="6615076069").split()))
SUDO_USERS.extend(FRIDAY)

OWNER_ID = int(getenv("OWNER_ID", default="6615076069"))
SUDO_USERS.append(OWNER_ID)

# Initialize Telegram client
X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
