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
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6809564656:AAFzMXyJ5Bqc7k4XjbCNfGPSj20RQhyUQzw")

# Admins list
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "6290483448").split(",") if i.strip()] if os.environ.get("ADMINS") else []
OWNER_ID = int(os.environ.get("OWNER_ID", "5549620776"))  # ID of the owner
if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)

# Database settings
DATABASE_NAME = os.environ.get("DATABASE_NAME", "UrlShortx24")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://vasanthtg8:vasanthtg8@cluster0.441zwwt.mongodb.net/?retryWrites=true&w=majority")  # MongoDB URI

# Optional variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001725631702"))  # Log channel for information about users
UPDATE_CHANNEL = int(os.environ.get("UPDATE_CHANNEL", "-1001409325739"))  # For force subscription
BROADCAST_AS_COPY = is_enabled(os.environ.get("BROADCAST_AS_COPY", "True"), False)  # True if forwarding should be avoided
IS_PRIVATE = is_enabled(os.environ.get("IS_PRIVATE", "False"), False)  # True for private use and restricting users
SOURCE_CODE = os.environ.get("SOURCE_CODE")  # For upstream repo
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", "https://graph.org/file/557eb3ed747c867c775d5.jpg")
LINK_BYPASS = is_enabled(os.environ.get("LINK_BYPASS", "False"), False)  # If true, URLs will be bypassed
BASE_SITE = os.environ.get("BASE_SITE", "")  # Your shortener site domain

# For Admin use
CHANNELS = is_enabled(os.environ.get("CHANNELS", "True"), True)
CHANNEL_ID = [int(i.strip()) for i in os.environ.get("CHANNEL_ID", "").split(" ") if i.strip()] if os.environ.get("CHANNEL_ID") else []
DE_BYPASS = [i.strip() for i in os.environ.get("DE_BYPASS", "").split(",") if i.strip()] if os.environ.get("DE_BYPASS") else []
if "mdisk.me" not in DE_BYPASS:
    DE_BYPASS.append("mdisk.me")

FORWARD_MESSAGE = is_enabled(os.environ.get("FORWARD_MESSAGE", "False"), False)  # True if forward message to be converted by reposting the post

WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "True"), True)
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "240"))
PORT = int(os.environ.get("PORT", "8000"))
