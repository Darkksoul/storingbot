#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "Devil")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6156013850"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", ""))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", ""))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/e6bb99215a5d7279b693c.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://te.legra.ph/file/9414371a5dbec3a2ca6ad.mp4")

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @DevilServers\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/DevilServersk>Devil</a></b>"
ABOUT_TXT = f"""
📁 Welcome to the Permanent FileStore Bot! 📁

📎 Send Me any Media or File and watch as the magic unfolds! Whether you're managing a Channel or just looking for a trusted file ally, I've got you covered. Add me to your Channel with Edit Permission, and I'll diligently store your uploaded files, providing you with a shareable link for seamless access and sharing.

🌟 It's that simple! Let's elevate your file management to a whole new level with the Permanent FileStore Bot. 👍

🔅 *FɪʟᴇSᴛᴏʀᴇBᴏᴛ* 🔅
  
🤖 **My Name**: [𝓕𝓲𝓵𝓮 𝓢𝓽𝓸𝓻𝓮 𝓑𝓸𝓽](https://t.me/{BOT_USERNAME})

📝 **Language**: [𝓟𝔂𝓽𝓱𝓸𝓷𝟑](https://www.python.org)

📚 **Library**: [𝓟𝔂𝓻𝓸𝓰𝓻𝓪𝓶](https://docs.pyrogram.org)

📡 **Hosted On**: [VPS](https://www.hostinger.com)

👨‍💻 **Developer**: [𝕯𝖊𝖛𝖎𝖑](https://t.me/DevilServers)

👥 **Bot Support**: [𝓢𝓾𝓹𝓹𝓸𝓻𝓽](https://t.me/DevilServers)

🔔 **Bot Updates**: [𝕌𝕡𝕕𝕒𝕥𝕖𝕤](https://t.me/DevilServers)

"""
START_MSG = os.environ.get("START_MESSAGE", """Hey there, [{}](tg://user?id={})\n\nI'm your very own Permanent FileStore Bot! 🤖**.

Want to know how to use me and all the amazing benefits I bring? Here's the lowdown:

📢 Simply send me any file and I'll upload it to my database, giving you a permanent link to access it anytime.

⚠️ Benefits: If you run a Telegram Any Channel or any other Stuff, I've got your back! Send me your files and I'll provide you with permanent links, keeping your channel safe from ©️. I even support channels - how cool is that? Check me out and see for yourself!

❌ Just remember, no +18 contents allowed! We take that seriously and it will result in a permanent ban.

So, what are you waiting for? Let's get started and make the most of all the awesome features I have to offer! 🌟
"""
try:
    ADMINS=[6156013850]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @DevilServers</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(6156013850)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
