import discord
from discord.ext import commands

#Define class
class RepCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Commands creation
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == 'こんにちは':
            await message.channel.send('こんにちは')

        if 'w' in message.content:
            await message.channel.send(random.choice(('www', '草')))
def setup(bot):
    bot.add_cog(RepCog(bot))
