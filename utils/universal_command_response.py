import discord
from discord.ext import commands

async def universal_command_response(ctx, message):
    if isinstance(ctx, commands.Context):
        await ctx.send(message)
    elif isinstance(ctx, discord.ApplicationContext):
        await ctx.respond(message, ephemeral=False)