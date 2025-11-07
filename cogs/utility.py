import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.slash_command()
    async def hello(self, ctx):
        user = ctx.author if isinstance(ctx, commands.Context) else ctx.user
        await ctx.respond(f"Hello, {user.mention}")

    @discord.slash_command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.respond(f"Pong! {latency}ms")
    
    @discord.slash_command()
    async def parrot(self, ctx, anon: bool, msg: str):
        user = "Anonymous" if anon else ctx.author.mention
        await ctx.respond(f"{user} said {msg}")

    @discord.slash_command()
    async def format(self, ctx, class_: str, module: str, topic: str):
        msg = f"**CLASS:** {class_}\n**MODULE:** {module}\n**TOPIC:** {topic}"
        await ctx.respond(msg)

    # EVENTS
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[Cog Utility] Ready – Bot User: {self.bot.user} (ID: {self.bot.user.id})")


# COG SETUP
def setup(bot: commands.Bot):
    cog = Utility(bot)
    bot.add_cog(cog)
