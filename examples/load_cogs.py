"""
This is a snippet of how to make the bot load cogs,
it does not include a bot object in the code,
there should already be one in the code where it's used
"""
bot = "A bot should be initialized here"

cogs_list = [
    'greetings',
    'moderation',
    'fun',
    'owner'
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')