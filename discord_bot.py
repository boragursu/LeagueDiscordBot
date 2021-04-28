import discord
from discord.ext import commands
import league

client = commands.Bot(command_prefix = ".")

def read_discord_token():
    with open("tokens.txt" , "r") as f:
        lines = f.readlines()
        return lines[0].strip()
discord_token = read_discord_token()

@client.event
async def on_ready():
    print("Bot is running!")
    print(league.output_player)
client.run(discord_token)

