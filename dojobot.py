import dotenv
from discord.ext import commands
import discord
from discord import app_commands
import os
import asyncio




dotenv.load_dotenv()#load the .env file into the environment

class DojoBot(commands.Bot):
    def __init__(self,commands_prefix,intents):
        intents = discord.Intents.all()
        intents.message_content = True
        intents.members= True
        
        
        super().__init__(commands_prefix,intents=intents)

        #environment variables
        self.TOKEN = os.getenv('DISCORD_TOKEN')
    
    async def sync_commands(self):
        try:
            await self.wait_until_ready()#let the bot log in
            #sync commands
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(f"Failed to sync commands: {e}")    
    
    @commands.Cog.listener()
    async def on_ready(self):   
        print(f"We have logged in as {self.user}")
        await self.sync_commands()
        #once the bot is ready, sync the commands
    
    #listen for a specific message    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == bot.user.id:
            return
        if "help" in message.content.lower():
            await message.channel.send("Command list: /create_category <category_name>")
        await bot.process_commands(message)    
    
    async def on_shutdown(self):
        print("Shutting down")
        await self.close()        
    
        
           
#initialize the bot to use in the main function        
bot = DojoBot(commands_prefix="/",intents=discord.Intents.all())


@bot.tree.command(name="create_category",description="Creates a category for a project")    
async def create_category(interaction: discord.Interaction ,category_name:str): 
    
    #roles that are allowed to use this command
    allowed_roles = ["Senor Programming Manager","Developer"]
    user = interaction.user 
    user_roles = [role.name for role in user.roles] #a list of roles belonging to the user who interacted with the command
    
    #test command to print out roles
    await interaction.response.send_message(f"User roles: {user_roles}")
    
    if any(role in allowed_roles for role in user_roles):
        guild = interaction.guild #get the guild the interaction happened in
        category=await guild.create_category(category_name)
        
        channels_to_create = ["kalendarz","ogolny","materialy"]
        channels = [await guild.create_text_channel(name=channel,category=category) for channel in channels_to_create]
        await interaction.followup.send(f"Created channels: {channels_to_create}")
        await interaction.followup.send(f"Created category: {category_name}")
        
@bot.tree.command(name="close_project",description="Deletes everything related to the project")
async def close_project(interaction:discord.Interaction,category_name:discord.CategoryChannel):
    #roles that are allowed to use this command
    allowed_roles = ["Senor Programming Manager","Developer"]
    user = interaction.user 
    user_roles = [role.name for role in user.roles] #a list of roles belonging to the user who interacted with the command
    
    if any(role in allowed_roles for role in user_roles):
        guild = interaction.guild
        delcategory = category_name
        channels = delcategory.channels
        try:
            [await channel.delete() for channel in channels]
        except Exception as e:
            print(f"Failed to delete channels: {e}")
        await delcategory.delete()    
        
        await interaction.response.send_message(f"Deleted category: {category_name}")
        
    
      
    

        
        
        
        
        
#stworz kategorie i  kanaly:
# kalendarz
#ogolny
#materialy   

#to do:
#komenda do:
#tworzenia bazowej struktury projektu
#zamykania projektu
#edytowania projektu (nazwa)
#dodawania/usuwania członków automatycznie dodających się do projektu z kanalu projekty

#jak czlonek projektu to automatycznie dostaje dostep do kanalu projektu (emojis z innego kanali ktory daje dostep do kanalu projektu)
