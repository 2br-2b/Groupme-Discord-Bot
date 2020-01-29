import discord
import asyncio
from discord.ext import tasks, commands

from groupme_files.groupme_post import send_groupme_message

class dmlistener(commands.Cog):
    def __init__(self, bot, channelid):
        self.bot = bot
        self.channelid = channelid

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.channel.id == self.channelid:
            return
        if message.author.bot:
            return    
            
        send_groupme_message(message.content)
