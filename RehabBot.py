import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
bot_prefix= "."
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
	
@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")
	
@client.command(pass_context=True)
async def creator(ctx):
    await client.say("My creator is the great Rehab!")
	
@client.command(pass_context=True)
async def botversion(ctx):
    await client.say("My version is currently v1.0.0")
	
@client.command(pass_context=True)
async def scooby (ctx):
    await client.say("Uh, like, Zoinks scoob!")
	
@client.command(pass_context=True)
async def easteregg (ctx):
    await client.say("But it's not Easter yet...")
	
@client.command(pass_context=True)
async def spiderman(ctx):
    await client.say("https://youtu.be/57ElWrJr_q8 ¯\_(ツ)_/¯")
	
@client.command(pass_context=True)
async def jakepaul (ctx):
    await client.say("Seriously? http://i0.kym-cdn.com/entries/icons/original/000/000/554/picard-facepalm.jpg ")
	
@client.command(pass_context=True)
async def franku (ctx):
    await client.say(" https://files.gamebanana.com/img/ico/sprays/572b66dabf387.gif ")
	
@client.command(pass_context=True)
async def jb (ctx):
    await client.say(" http://i1.kym-cdn.com/photos/images/newsfeed/001/162/161/736.gif ")
	
	

	
client.run("MzU5NzA2NDg4Mjk5NzE2NjA4.DKK7hA.DVFlMX6CjhBXo6pSm8J1U6eP3iE")
