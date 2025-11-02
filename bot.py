import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

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

bot.load_extension("cogs.utility")
bot.run(token)