import discord
import discord_files.dmlistener
from discord_files.dmlistener import dmlistener
from discord.ext import commands
from discord_files.token_manager import TOKEN as TOKEN

from groupme_files.groupme_post import send_groupme_message

channelID = 672156344157077560

bot = commands.Bot("g.")
dml = dmlistener(bot, channelID)
bot.add_cog(dml)

@bot.event
async def on_ready():
    print("Started!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" for groupme"))

bot.run(TOKEN)
