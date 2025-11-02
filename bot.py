import discord
import os
from dotenv import load_dotenv

# Get Bot Token
load_dotenv() # Lods all variables from the env file
token = os.getenv('TOKEN') # Bot token

# Initialize Bot
bot = discord.Bot()

# Ready Event
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

bot.run(token)