import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

### Load environment variables ###
load_dotenv()

# Grab our client secret
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

####
####        IF YOU NEED HELP, LOOK UP THE discord.py DOCUMENTATION
####        https://discordpy.readthedocs.io/en/latest/index.html
####

#   CompSci and Tech (testing guild) info
bot_channel_id = 816185156679368736  # bot-experimentation
test_guild_id = 813897870566490122  # compsci

#TODO: add dependency folder

# for the functions
#import functions

from on_message import receive_message

description = "This is the TUB bot <3"
intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix=";", description=description, intents=intents)
client = discord.Client(intents=intents)
# the above line is similar to client = discord.Client(intents=intents)


  # TODO: INSERT TESTING USER HERE


@client.event
async def on_ready():  # when the bot is ready to do things (on discord)
    await client.wait_until_ready()
    bot_channel = client.get_channel(bot_channel_id)
    # TODO: figure out why the fuck this works
    print('logged in as {0.user}'.format(client))
    await bot_channel.send("""
***HEY, I'M THE TUB_ BOT!***\n
I am now running, and (semi-)functional!""")


@client.event
async def on_message(message):

    # Logic upon receiving a message is to be customised in on_message.py
    await receive_message(client, message)


# THIS IS A SECRET FOR ONLY US
client.run(CLIENT_SECRET)
