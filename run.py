import dojobot as dj
import asyncio
import discord


async def main():
    discord.utils.setup_logging()#shows errors
    await dj.bot.start(dj.bot.TOKEN)
    
if __name__ == "__main__":
    asyncio.run(dj.bot.start(dj.bot.TOKEN))     