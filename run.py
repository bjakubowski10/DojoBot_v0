import dojobot as dj
import asyncio
import discord


async def main():
    discord.utils.setup_logging()#shows errors
    await bot.start(bot.TOKEN)
    
if __name__ == "__main__":
    bot = dj.DojoBot(commands_prefix="/")
    #bot.add_cog(DojoBot(bot)) #will be used if using separate files for cogs
    asyncio.run(bot.start(bot.TOKEN))     