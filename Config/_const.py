import discord, os
from datetime import datetime

# These are both secret, so I keep them as environment variables
TOKEN = os.getenv("BRAIN_TOKEN") # Bot's token
DB_LINK = os.getenv("BRAIN_DB") # Postgres DB link

BRAIN = discord.Client() # The bot object

CURRENT_DAY = datetime.utcnow().day # For event handler purposes

PREFIX = "tc/" # Command prefix

STAFF_ID = 481991172106092554 # Staff role
TWOW_CENTRAL_ID = 481509601590771724 # Server
MEMBER_ID = 481950361783894017 # Member role

PUBLIC_CHANNELS = (
	481509602035236865, #general
	481534463608619038, #rec-room
	598616636823437352, #game-room
	481535292541501452, #twow-discussion
	481534865045717013, #art-studio
	481534925997211658, #server-discussion
	481534942279630856, #bots-memes
	534909693580017685, #voting
	481535329199980564, #general-hosting
	481549073401511952, #aesthetics
	481549091298344961, #technologies
	481549106662211588, #presentation
	481549059656777739, #innovations
	614117909693857819  #vc-general
)

BOT_CHANNELS = (
	481534942279630856, #bots-memes
	598616636823437352  #game-room
)

GAME_CHANNEL = 598616636823437352 #game-room
LOG_CHANNEL = 653677748832698378 #brain-logs

# For MMT purposes
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"