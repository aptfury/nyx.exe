from functools import wraps
import discord
from discord.ext import commands

def universal_command_wrapper(name: str, description: str):
    """
    Decorator to mark a coroutine as a command that should be registered
    as both a prefix command and a slash command.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(self, source):
            await func(self, source)

        # Metadata for registration
        wrapper._is_prefix_command = True
        wrapper._prefix_name = name
        wrapper._is_slash_command = True
        wrapper._slash_name = name
        wrapper._slash_description = description
        return wrapper
    return decorator

async def universal_command_response(ctx, message):
    if isinstance(ctx, commands.Context):
        await ctx.send(message)
    elif isinstance(ctx, discord.ApplicationContext):
        await ctx.respond(message, ephemeral=False)