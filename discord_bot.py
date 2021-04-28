import discord
from discord.ext import commands
import league
from league import printOutPlayerData

client = commands.Bot(command_prefix = ".")

def read_discord_token():
    with open("tokens.txt" , "r") as f:
        lines = f.readlines()
        return lines[0].strip()
discord_token = read_discord_token()

@client.event
async def on_ready():
    print("Bot is running!")

@client.command()
async def leaguestat(ctx, inputted_name):
    print(inputted_name)
    result = printOutPlayerData(str(inputted_name))
    await ctx.send(result)
client.run(discord_token)


