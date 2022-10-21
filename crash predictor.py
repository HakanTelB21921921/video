# This script was made by Sallanan Kedi
# Thanks For Using This Code

import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.command()
async def crash(ctx):
    prediction = round(random.uniform(1, 6), 2)
    em = discord.Embed(color=0xA928DD)
    em.add_field(name="Bloxflip Crash Predictor", value=prediction)
    await ctx.send(embed=em)


bot.run('Discord Botunuzun Tokeni / Your Discord Bots Token')
