import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Get Bot Token
load_dotenv() # Lods all variables from the env file
token = os.getenv('TOKEN') # Bot token

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Initialize Bot
bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

# --------------------------
# Events
# --------------------------
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ({bot.user.id})")
    print("------")

# --------------------------
# Automatic cog loader
# --------------------------
cogs_dir = "cogs"
for filename in os.listdir(cogs_dir):
    if filename.endswith(".py") and not filename.startswith("__"):
        cog_name = f"{cogs_dir}.{filename[:-3]}"
        try:
            bot.load_extension(cog_name)
            print(f"Loaded cog: {cog_name}")
        except Exception as e:
            print(f"Failed to load cog {cog_name}: {e}")

# bot.load_extension("cogs.utility")
bot.run(token)