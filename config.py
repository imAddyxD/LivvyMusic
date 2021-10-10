import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
OWNER_NAME = getenv("OWNER_NAME", "RhythmOff")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "RhythmOfficial")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/62481e4230d8a5c438840.jpg")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_ID = int(os.environ.get("OWNER_ID"))
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "LivvyMusic")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "RhythmOff")
PROJECT_NAME = getenv("PROJECT_NAME", "Livvy Music")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/imAddyxD/LivvyMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
