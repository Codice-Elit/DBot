import discord
import json
import random 
from discord.ext import commands, tasks
from itertools import cycle
import os
token = "Nzc4OTk0ODI2OTQyODczNjIw.X7aFdw.dcMHAmstnVfRIT74gRUuLUUcVyQ" 
'''
set_token = input("Choose bot: ")
if(set_token == "1"):
    token = ""

elif(set_token == "2"):
        token = ""
'''
def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guilds.id)]

client = commands.Bot(command_prefix = get_prefix)
status = cycle(['>help', 'There Is No Game', '>help', 'Plague.inc', '>help', 'Among Us', '>help', 'Cyberpunk 2077'])

version_1 = "alpha 0.1"
@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game('>help'))
    change_status.start()
    os.system("cls")
    guilds = client.guilds
    name = client.user
    latency = client.latency * 1000
    print(f"                                            Connected as {name}")
    print(f"                                        Bot latency = {latency}ms")
    print("------------------------------------------------------------------------------------------------------------------------")


@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    #prefixes[str(guild.id)]


@client.command(aliases=["latency"])                                                                                                #<==Ping cmd
async def ping(ctx):
    await ctx.send(f"Pong! {client.latency * 1000}ms")


@client.command(aliases=['8ball', '8b'])                                                                                            #<==8Ball cmd
async def _8ball(ctx, *, question):
    responses = [
        'It is decidedly so.'           ,
        'Without a doubt.'              ,
        'Yes – definitely.'             ,
        'You may rely on it.'           ,
        'As I see it, yes.'             ,
        'Most likely.'                  ,
        'Outlook good.'                 ,
        'Yes.'                          ,
        'Signs point to yes.'           ,
        'Reply hazy, try again.'        ,
        'Ask again later.'              ,
        'Better not tell you now.'      ,
        'Cannot predict now.'           ,
        'Concentrate and ask again.'    ,
        'Do not count on it.'           ,
        'My reply is no.'               ,
        'My sources say no.'            ,
        'Outlook not so good.'          ,
        'Very doubtful.'
        ]
    
    embed = discord.Embed(
        title = 'THE MAGIC 8BALL REPLIES',
        desc = f'Question: {question}\nAnswer: {random.choice(responses)}',
        colour = discord.Colour.teal(),
        )
    await ctx.send()


@client.command()                                                                                                                   #<==Hyperlink cmd
async def hl(ctx, *, linkName, heading, link):
    hyperLink = discord.Embed(
        title='{linkName}',
        description='[{heading}]({link})',
        color=discord.Colour.teal()
    )
    await ctx.send(embed = hyperLink)
    pass



@client.command()                                                                                                                   #<==Clear cmd
async def clear(ctx, amount = 5):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)



@client.command()                                                                                                                   #<==Kick cmd
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)



@client.command()                                                                                                                   #<==Ban cmd
@commands.has_permissions(ban_members=True)
async def ban(ctx, user : discord.Member, *, reason = "No Reason Specified"):
    await user.ban(reason = reason)
    await ctx.send(f'Banned {user.mention}')



@client.command()                                                                                                                   #<==Unban cmd
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return



@client.command(aliases=["dm","dm_send"])
async def send_dm(ctx, member: discord.Member, *, content):
        channel = await member.create_dm()
        await channel.send(content)


client.run(token)