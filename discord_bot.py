import discord
from discord.ext import commands
from league import *

client = commands.Bot(command_prefix = ".", help_command=None)

def read_discord_token():
    with open("tokens.txt" , "r") as f:
        lines = f.readlines()
        return lines[0].strip()
discord_token = read_discord_token()

@client.event
async def on_ready():
    print("Bot is running!")

@client.command(pass_context = True)
async def helplolstat(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour= discord.Colour.red()
    )
    embed.set_author(name= "Help")
    embed.add_field(name = " usage lolstat {summoner name} {region code}", value = "Returns basic summoner stats", inline = False)

    await ctx.send(embed=embed)

@client.command()
async def lolflexstat(ctx, inputted_name, my_region):
    print(inputted_name)
    result = printOutFlexPlayerData(str(inputted_name), my_region)
    await ctx.send(result)

@client.command()
async def lolstat(ctx, inputted_name, my_region):  
    print(inputted_name)
    result = printOutPlayerData(str(inputted_name), my_region)
    summonericon=showSummonerIcon(str(inputted_name), my_region)
    print(result)
    print(summonericon)

    embed_stat = discord.Embed(
        colour = discord.Colour.red()
    )
    embed_stat.set_author(name = "Ranked Solo/Duo")
    embed_stat.add_field(name = "Summoner rank", value=result, inline=True)
    embed_stat.set_footer(icon_url=ctx.author.avatar_url, text =f"Requested by {ctx.author.name}" )
    embed_stat.set_thumbnail(url=summonericon)
    await ctx.send(embed=embed_stat)

""" @lolflexstat.error
async def lolflexstat_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
        await ctx.send("Username not found in the selected region, doesn't exist or unranked in flex queue for more information about the command write .helplolflexstat")
 """

""" @lolstat.error
async def lolstat_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
        await ctx.send("Username not found in the selected region, doesn't exist or unranked in solo/duo queue")
 """
client.run(discord_token)