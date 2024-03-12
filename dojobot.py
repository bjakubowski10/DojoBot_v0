import dotenv
from discord.ext import commands
import discord
import os
import asyncio




dotenv.load_dotenv()#load the .env file into the environment

class DojoBot(commands.Bot):
    def __init__(self,commands_prefix):
        intents = discord.Intents.all()
        intents.message_content = True
        intents.members= True
        
        super().__init__(commands_prefix,intents=intents)
        
        
        #environment variables
        self.TOKEN = os.getenv('DISCORD_TOKEN')
    
    async def sync_commands(self):
        #sync commands
        try:
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} commands")
        except Exception as e:
            print(f"Failed to sync commands: {e}")    
        
    
    @commands.Cog.listener()
    async def on_ready(self):   
        print(f"We have logged in as {self.user}")
        await self.sync_commands()
    
    async def on_shutdown(self):
        print("Shutting down")
        await self.close()    
        
             
        
        
        


#bot = DojoBot(commands_prefix="/")

#to do:
#komenda do:
#tworzenia bazowej struktury projektu
#zamykania projektu
#edytowania projektu (nazwa)
#dodawania/usuwania członków automatycznie dodających się do projektu z kanalu projekty
