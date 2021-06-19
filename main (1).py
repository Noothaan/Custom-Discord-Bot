import discord
import os
from keep_alive import keep_alive

from discord.ext import commands

import random
import time
import asyncio

client = commands.Bot(command_prefix = '>')
#remove help command for a nicer version
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('>help for more info'))
    print('System Online: {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(f'{member} joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} left a server')
#commands
@client.command()
async def skye(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/855785866127343616/855868457730834472/BoYRMteyQBOo9hgM2TO0.png')

@client.command()
async def latency(ctx):
    await ctx.send(f'Latency: {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["As I see it, yes.", "Ask again later.", "Possibly... (no.)", "Nah ur retarded.",
                 "Nah shutup.",
                 "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.",
                 "My sources say no.",
                 "Outlook says fuck no.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.",
                 "Def lad.", "Ofc mate.",
                 "Yes.", "Yes well in lad.", "You may rely on it."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
#Chad command
@client.command()
async def noothan(ctx):
    await ctx.send('https://media.tenor.com/images/a7ab88c1dc364a0325334b6df4b4269c/tenor.gif')
#Clear command
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

#Invalid command
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid prefix usage, type >help for a list of commands")

#Help commands
@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="Help", description="Usage: >help [command] for info")

    em.add_field(name="Moderation", value="clear,")
    em.add_field(name="Hall Of Fame", value="skye, noothan")

    await ctx.send(embed=em)

@help.command()
async def clear(ctx):
    em = discord.Embed(title="Clear", description="Clears messages (Defaulted to 5)")
    em.add_field(name="**Usage**", value=">Clear [amount]")

    await ctx.send(embed=em)

@help.command()
async def skye(ctx):
    em = discord.Embed(title="Skye", description="Shows a real image of the retarded owner of this server")
    em.add_field(name="**Usage**", value=">skye")

    await ctx.send(embed=em)

@help.command()
async def noothan(ctx):
    em = discord.Embed(title="noothan", description="Shows a real image of the chad creator of this bot")
    em.add_field(name="**Usage**", value=">noothan")

    await ctx.send(embed=em)


keep_alive()
client.run(os.getenv('TOKEN'))