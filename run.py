import dojobot as dj
import asyncio
import discord
import logging


async def main():
    logging.basicConfig(level=logging.INFO)
    discord.utils.setup_logging(level=logging.INFO, root=False)    
if __name__ == "__main__":
    asyncio.run(dj.bot.run(dj.bot.TOKEN))     