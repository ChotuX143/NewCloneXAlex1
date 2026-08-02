import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
BOT_ID = getenv("BOT_ID")

OWNER_USERNAME = getenv("OWNER_USERNAME", "")
BOT_USERNAME = getenv("BOT_USERNAME", "")
BOT_NAME = getenv("BOT_NAME", "")
ASSUSERNAME = getenv("ASSUSERNAME", "")
BOT_LINK = getenv("BOT_LINK", "https://t.me/TomXClonerBot")

MONGO_DB_URI = getenv("MONGO_DB_URI")

# ✅ JioSaavn Working API Added Here
JIOSAAVN_API = getenv("JIOSAAVN_API", "https://saavn.me/search/songs?query=")

# ----------------- API RACING CONFIGURATION -----------------
# 1. Shruti API
API_URL = getenv("API_URL", "https://api.shrutibots.site")
API_KEY = getenv("API_KEY", "ShrutiBotsZa1SAoubJ7OqtKHZbDgu")

# 2. Xbit API
YTPROXY_URL = getenv("YTPROXY_URL", "https://tgapi.xbitcode.com")
YT_API_KEY = getenv("YT_API_KEY" , "xbit_B4TNnBAoe6uoSM7NLFz-dk6X7GibJ6Bh")

# 3. Worker API
WORKER_FALLBACK_API_URL = getenv("WORKER_FALLBACK_API_URL", "https://youtubenewapi.skybotsdeveloper.workers.dev")
WORKER_FALLBACK_API_KEY = getenv("WORKER_FALLBACK_API_KEY", "itsmesid")

# 4. Inflex API
INFLEX_API_URL = getenv("INFLEX_API_URL", "https://teaminflex.xyz")
INFLEX_API_KEY = getenv("INFLEX_API_KEY", "INFLEX47405528D")



DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000000))

LOGGER_ID = int(getenv("LOGGER_ID", "0"))
LOGGER_2_ID = int(getenv("LOGGER_2_ID", "-1002645692318"))
CLONE_LOGGER = LOGGER_ID
CLONE_LOGGER_2 = int(getenv("CLONE_LOGGER_2", "-1002645692318")) # ✅ Yahan naya Log Group 2 add kiya hai

OWNER_ID = int(getenv("OWNER_ID", "5555422614"))

# 🟢 THE FIX: SUDOERS LIST ADDED HERE WITH YOUR IDS
SUDOERS = [5555422614, 6556974543]

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ChotuX143/NewCloneXAlex1",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", "")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TitanNetwrk")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Musical_Beatsz")
GITHUB = getenv("GITHUB", "https://t.me/Telugu_Grpz")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "99999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "99999999"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "63f2d3fb20c84cfaa472e5c3b805cd6b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c0b5b18383c2447fb9bd13f7eae42a57")

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
PLAYLIST_ID = -1003812209413

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# 🟢 4 ASSISTANT SESSIONS ADDED HERE
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", "")
STRING3 = getenv("STRING_SESSION3", "")
STRING4 = getenv("STRING_SESSION4", "")

START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/euxbyi.png").split()
HELP_IMG_URL = getenv("HELP_IMG_URL", "https://telegra.ph/file/c316aa782ab03f45ba9c2.jpg").split()
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/64dacee61bdf2365497ef.jpg").split()

PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL", "https://telegra.ph/file/c316aa782ab03f45ba9c2.jpg https://files.catbox.moe/92cq9y.png https://files.catbox.moe/ovkpoo.png https://files.catbox.moe/ovkpoo.png").split()
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://files.catbox.moe/601kug.jpg")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL", "https://files.catbox.moe/ovkpoo.png").split()
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL", "https://files.catbox.moe/ovkpoo.png").split()
STREAM_IMG_URL = getenv("STREAM_IMG_URL", "https://files.catbox.moe/ovkpoo.png").split()
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL", "https://i.ibb.co/S4sPf3q8/soundcloud.jpg").split()
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://files.catbox.moe/ovkpoo.png").split()
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL", "https://i.ibb.co/XZfMS8Db/spotify.jpg").split()
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL", "https://i.ibb.co/XZfMS8Db/spotify.jpg").split()
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL", "https://i.ibb.co/XZfMS8Db/spotify.jpg").split()

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/d4yhs6.png").split()

def time_to_seconds(time):
    return sum(int(x) * 60**i for i, x in enumerate(reversed(str(time).split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL url must start with https://")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT url must start with https://")

CMBOT = [ "💞", "🥂", "🔍", "🧪", "⚡️", "🔥", "🦋", "🎩", "🌈", "🍷",
    "🥃", "🥤", "🕊️", "💌", "🧨", "✨", "💥", "💯", "🌟", "⚡️",
    "❤️", "😍", "🥰", "😘", "😂", "🤣", "😱", "😡", "👏", "🙏",
    "🎉", "🎊", "🎶", "🎵", "🎧", "🎸", "🎹", "🥁", "🎺", "🎷",
    "🔥", "⚡️", "💫", "🌙", "☀️", "🌈", "❄️", "🌸", "🌺", "🌹",
    "🦋", "🕊️", "🐍", "🐯", "🦁", "🐺", "🐉", "🦅", "🦄", "🐎"

    ]

EFFECT_ID = [
    5046509860389126442,
    5107584321108051014,
    5104841245755180586,
    5159385139981059251,
]
