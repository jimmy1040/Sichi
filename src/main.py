import os
import discord
from dotenv import load_dotenv

load_dotenv()

bot = discord.Client(intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot is ready!")


bot.run(os.getenv('TOKEN'))
