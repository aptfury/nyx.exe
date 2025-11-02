import discord
from discord.ext import commands
from utils.universal_command import universal_command
from utils.universal_command_response import universal_command_response

class Utility(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # COMMANDS
    @universal_command(name="hello", description="Say hello")
    async def hello(self, source):
        user = source.author if isinstance(source, commands.Context) else source.user
        await universal_command_response(source, f"Hello, {user.mention}!")

    @universal_command(name="ping", description="Check bot latency")
    async def ping(self, source):
        latency = round(self.bot.latency * 1000)
        await universal_command_response(source, f"Pong! {latency}ms")

    # EVENTS
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[Cog Utility] Ready – Bot User: {self.bot.user} (ID: {self.bot.user.id})")


# COG SETUP
def setup(bot: commands.Bot):
    cog = Utility(bot)
    bot.add_cog(cog)

    # Register slash commands after Cog is added
    for attr_name in dir(cog):
        attr = getattr(cog, attr_name)
        if callable(attr) and getattr(attr, "_is_slash_command", False):
            bot.slash_command(
                name=attr._slash_name,
                description=attr._slash_description
            )(attr)

    # Register prefix commands after Cog is added
    for attr_name in dir(cog):
        attr = getattr(cog, attr_name)
        if callable(attr) and getattr(attr, "_is_prefix_command", False):
            bot.add_command(commands.Command(attr, name=attr._prefix_name))
