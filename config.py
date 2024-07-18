import os
from dotenv import load_dotenv

load_dotenv()

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Mandatory variables for the bot to start
# API ID from https://my.telegram.org/auth
API_ID = int(os.environ.get("API_ID", "24025974"))
# API Hash from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH", "2abf0406f41a57b540bdefe8b12d114f")
# Bot token from @BotFather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
# Admin IDs
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "6290483448").split(",") if i.strip().isdigit()]

DATABASE_NAME = os.environ.get("DATABASE_NAME", "UrlShortx24")
# MongoDB URI from https://www.mongodb.com/
DATABASE_URL = os.environ.get(
    "DATABASE_URL", "mongodb+srv://vasanthtg8:vasanthtg8@cluster0.441zwwt.mongodb.net/?retryWrites=true&w=majority"
)
# Owner ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5549620776"))
if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)

# Optional variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001725631702"))
# For Force Subscription
UPDATE_CHANNEL = int(os.environ.get("UPDATE_CHANNEL", "-1001409325739"))
BROADCAST_AS_COPY = is_enabled(os.environ.get("BROADCAST_AS_COPY", "True"), False)
IS_PRIVATE = is_enabled(os.environ.get("IS_PRIVATE", "False"), False)
SOURCE_CODE = os.environ.get("SOURCE_CODE")
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", "https://graph.org/file/557eb3ed747c867c775d5.jpg")
LINK_BYPASS = is_enabled(os.environ.get("LINK_BYPASS", "False"), False)
BASE_SITE = os.environ.get("BASE_SITE", "")

# For Admin use
CHANNELS = is_enabled(os.environ.get("CHANNELS", "True"), True)
CHANNEL_ID = [int(i.strip()) for i in os.environ.get("CHANNEL_ID", "").split(" ") if i.strip().isdigit()]

DE_BYPASS = [i.strip() for i in os.environ.get("DE_BYPASS", "").split(",") if i.strip()]
DE_BYPASS.append("mdisk.me")

FORWARD_MESSAGE = is_enabled(os.environ.get("FORWARD_MESSAGE", "False"), False)

WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "True"), True)
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "240"))
PORT = int(os.environ.get("PORT", "8000"))
