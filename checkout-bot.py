import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Set intents necessary for the Bot class to function
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot with a command prefix
bot = commands.Bot(command_prefix='/', intents=intents)

# List of total available accounts
active_users = [(os.getenv("USER01")), (os.getenv("USER02")), (os.getenv("USER03")), (os.getenv("USER04")), (os.getenv("USER05"))] 

# Check out command - removes a user from the active list
@bot.command()
async def checkout(ctx, name: str):
    if name in active_users:
        active_users.remove(name)
        await ctx.send(f"User {name} has been checked out and removed from the active list.")
    else:
        await ctx.send(f"User {name} is not in the active list.")

# Free up command - adds a user back to the active list
@bot.command()
async def freeup(ctx, name: str):
    if name not in active_users:
        active_users.append(name)
        await ctx.send(f"User {name} has been added back to the active list.")
    else:
        await ctx.send(f"User {name} is already in the active list.")

# Run the bot with your token
bot.run((os.getenv("API_TOKEN"))) 