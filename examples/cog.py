"""
These examples come from pycord.dev.
I'm including them here for reference materials while building.
This is not a part of the bot's funcionality,
and it exists solely to avoid re-opening and closing the site.
"""

import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() # creates a prefixed command
    async def hello(self, ctx):
        await ctx.send('Hello!')

    @discord.slash_command() # creates a slash command
    async def goodbye(self, ctx):
        await ctx.respond('Goodbye!')

    @discord.user_command() # creates a command in the user context menu
    async def greet(self, ctx, member: discord.Member):
        await ctx.respond(f"{ctx.author.mention} says hello to {member.mention}!")

    """
    Slash Command Group Example
    """
    math = discord.SlashCommandGroup("math", "Spooky math stuff") # creates a slash command group named 'math'
    advanced_math = math.create_subgroup(
        "adbanced",
        "super hard math commands"
    )

    @math.command()
    async def add(self, ctx, a: int, b: int):
        c = a + b
        await ctx.respond(f"{a} + {b} = {c}")

    @advanced_math.command()
    async def midpoint(self, ctx, x1: float, y1: float, x2: float, y2: float):
        mid_x = (x1 + x2)/2
        mid_y = (y1 + y2)/2
        await ctx.respond(f"The midpoint between those coordinates is ({mix_x, {mid_y}})")

    @commands.Cog.listener()
    async def on_member_join(self, member): # Listener that activates when someone joins
        # Must have the proper intents
        await member.send('Welcome to the server!')

def setup(bot):
    bot.add_cog(Greetings(bot))